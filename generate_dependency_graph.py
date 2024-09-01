import os
import ast
import json
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def get_imports(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            tree = ast.parse(file.read())
    except UnicodeDecodeError:
        print(f"Warning: Unable to parse {file_path} due to encoding issues. Skipping this file.")
        return []
    
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module if node.module else ''
            for alias in node.names:
                imports.append(f"{module}.{alias.name}")
    
    return imports

def generate_dependency_graph(directory, ignore_dirs=None, max_depth=3):
    if ignore_dirs is None:
        ignore_dirs = ['venv', 'env', '__pycache__']
    
    dependencies = {}
    project_files = set()
    
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        depth = root[len(directory):].count(os.path.sep)
        if depth > max_depth:
            continue
        
        for file in files:
            if file.endswith('.py'):
                module_name = os.path.splitext(file)[0]
                project_files.add(module_name)
    
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        depth = root[len(directory):].count(os.path.sep)
        if depth > max_depth:
            continue
        
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                module_name = os.path.splitext(file)[0]
                
                imports = get_imports(file_path)
                dependencies[module_name] = [imp.split('.')[0] for imp in imports 
                                             if imp.split('.')[0] in project_files]

    # Berechne zusätzliche Metriken
    import_count = defaultdict(int)
    for deps in dependencies.values():
        for dep in deps:
            import_count[dep] += 1

    # Bestimme Modultypen
    core_modules = {mod for mod, count in import_count.items() if count > 3}
    utility_modules = {mod for mod in dependencies if mod.endswith('_utils') or mod == 'config'}
    test_modules = {mod for mod in dependencies if mod.startswith('test_')}

    # Generiere die verbesserte DOT-Datei
    with open('dependency_graph.dot', 'w') as f:
        f.write("digraph DependencyGraph {\n")
        f.write("    rankdir=LR;\n")
        f.write("    node [shape=box, style=filled];\n")
        
        # Definiere Subgraphen für Gruppierung
        f.write("    subgraph cluster_core {\n")
        f.write("        label = \"Core Modules\";\n")
        f.write("        style = filled;\n")
        f.write("        color = lightgrey;\n")
        for module in core_modules:
            size = 1 + import_count[module] * 0.5  # Größe basierend auf Importanzahl
            f.write(f'        "{module}" [fillcolor=lightblue, width={size}, height={size}];\n')
        f.write("    }\n")

        f.write("    subgraph cluster_utility {\n")
        f.write("        label = \"Utility Modules\";\n")
        f.write("        style = filled;\n")
        f.write("        color = lightyellow;\n")
        for module in utility_modules:
            f.write(f'        "{module}" [fillcolor=yellow];\n')
        f.write("    }\n")

        f.write("    subgraph cluster_test {\n")
        f.write("        label = \"Test Modules\";\n")
        f.write("        style = filled;\n")
        f.write("        color = lightgreen;\n")
        for module in test_modules:
            f.write(f'        "{module}" [fillcolor=green];\n')
        f.write("    }\n")

        # Füge restliche Module hinzu
        other_modules = set(dependencies.keys()) - core_modules - utility_modules - test_modules
        for module in other_modules:
            f.write(f'    "{module}" [fillcolor=white];\n')

        # Füge Kanten hinzu
        for module, deps in sorted(dependencies.items()):
            for dep in sorted(deps):
                f.write(f'    "{module}" -> "{dep}";\n')
        
        f.write("}\n")
    
    print("Enhanced dependency graph generated: dependency_graph.dot")

    # Generate .txt file
    with open('dependency_graph.txt', 'w') as f:
        for module, deps in sorted(dependencies.items()):
            if deps:
                f.write(f"{module}:\n")
                for dep in sorted(deps):
                    f.write(f"  - {dep}\n")
                f.write("\n")
    
    print("Dependency graph generated: dependency_graph.txt")

    # Generate .png file
    G = nx.DiGraph()
    for module, deps in dependencies.items():
        for dep in deps:
            G.add_edge(module, dep)
    
    plt.figure(figsize=(20, 15))
    pos = nx.spring_layout(G, k=0.9, iterations=50)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, 
            font_size=8, font_weight='bold', arrows=True, 
            edge_color='gray', width=0.5, arrowsize=20)
    
    plt.title("Dependency Graph", fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('dependency_graph.png', format='png', dpi=300, bbox_inches='tight')
    plt.close()

    print("Dependency graph generated: dependency_graph.png")

    # Generiere JSON für interaktive Visualisierung
    graph_data = {
        "nodes": [{"id": mod, "group": 1 if mod in core_modules else 2 if mod in utility_modules else 3 if mod in test_modules else 4} for mod in dependencies],
        "links": [{"source": mod, "target": dep, "value": 1} for mod, deps in dependencies.items() for dep in deps]
    }
    
    with open('dependency_graph.json', 'w') as f:
        json.dump(graph_data, f)

    print("JSON data generated for interactive visualization: dependency_graph.json")

    # Generiere HTML für interaktive Visualisierung
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Dependency Graph</title>
        <script src="https://d3js.org/d3.v5.min.js"></script>
        <style>
            .node { stroke: #fff; stroke-width: 1.5px; }
            .link { stroke: #999; stroke-opacity: 0.6; }
        </style>
    </head>
    <body>
        <svg width="960" height="600"></svg>
        <script>
            d3.json("dependency_graph.json").then(function(graph) {
                var svg = d3.select("svg"),
                    width = +svg.attr("width"),
                    height = +svg.attr("height");

                var color = d3.scaleOrdinal(d3.schemeCategory10);

                var simulation = d3.forceSimulation()
                    .force("link", d3.forceLink().id(function(d) { return d.id; }))
                    .force("charge", d3.forceManyBody())
                    .force("center", d3.forceCenter(width / 2, height / 2));

                var link = svg.append("g")
                    .attr("class", "links")
                    .selectAll("line")
                    .data(graph.links)
                    .enter().append("line")
                    .attr("stroke-width", function(d) { return Math.sqrt(d.value); });

                var node = svg.append("g")
                    .attr("class", "nodes")
                    .selectAll("circle")
                    .data(graph.nodes)
                    .enter().append("circle")
                    .attr("r", 5)
                    .attr("fill", function(d) { return color(d.group); })
                    .call(d3.drag()
                        .on("start", dragstarted)
                        .on("drag", dragged)
                        .on("end", dragended));

                node.append("title")
                    .text(function(d) { return d.id; });

                simulation
                    .nodes(graph.nodes)
                    .on("tick", ticked);

                simulation.force("link")
                    .links(graph.links);

                function ticked() {
                    link
                        .attr("x1", function(d) { return d.source.x; })
                        .attr("y1", function(d) { return d.source.y; })
                        .attr("x2", function(d) { return d.target.x; })
                        .attr("y2", function(d) { return d.target.y; });

                    node
                        .attr("cx", function(d) { return d.x; })
                        .attr("cy", function(d) { return d.y; });
                }

                function dragstarted(d) {
                    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
                    d.fx = d.x;
                    d.fy = d.y;
                }

                function dragged(d) {
                    d.fx = d3.event.x;
                    d.fy = d3.event.y;
                }

                function dragended(d) {
                    if (!d3.event.active) simulation.alphaTarget(0);
                    d.fx = null;
                    d.fy = null;
                }
            });
        </script>
    </body>
    </html>
    """

    with open('dependency_graph.html', 'w') as f:
        f.write(html_content)

    print("Interactive HTML visualization generated: dependency_graph.html")

if __name__ == "__main__":
    project_directory = "."  # Current directory, change if needed
    generate_dependency_graph(project_directory)