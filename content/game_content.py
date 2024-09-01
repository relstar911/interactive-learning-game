# HR Manager Quiz
HR_QUESTIONS = [
    {
        "question": "What is the primary role of HR?",
        "options": ["Hiring", "Firing", "Employee Well-being", "All of the above"],
        "correct": 3
    },
    {
        "question": "Which of these is NOT typically an HR responsibility?",
        "options": ["Payroll", "Training", "Product Development", "Conflict Resolution"],
        "correct": 2
    },
    {
        "question": "What is the purpose of an employee handbook?",
        "options": ["To entertain employees", "To outline company policies and procedures", "To list employee salaries", "To provide cooking recipes"],
        "correct": 1
    },
    {
        "question": "What does 'onboarding' refer to in HR?",
        "options": ["Firing employees", "The process of integrating new employees", "A type of water sport", "Annual performance reviews"],
        "correct": 1
    },
    {
        "question": "Which of these is an example of workplace diversity?",
        "options": ["All employees are the same age", "Employees from different cultural backgrounds", "Only hiring one gender", "Everyone has the same job title"],
        "correct": 1
    },
    {
        "question": "What is the purpose of a performance review?",
        "options": ["To criticize employees", "To evaluate and improve employee performance", "To decide on pay cuts", "To plan office parties"],
        "correct": 1
    },
    {
        "question": "What does 'diversity and inclusion' mean in the workplace?",
        "options": ["Hiring only minorities", "Creating a work environment that represents and values different backgrounds", "Excluding certain groups", "Focusing only on gender equality"],
        "correct": 1
    },
    {
        "question": "What is the primary purpose of an employee assistance program (EAP)?",
        "options": ["To spy on employees", "To provide support for personal and work-related issues", "To increase workload", "To reduce salaries"],
        "correct": 1
    }
]

# IT Specialist Role-Play Scenarios
IT_SCENARIOS = [
    {
        "situation": "A colleague's computer won't turn on. What's your first step?",
        "options": [
            {"text": "Check if it's plugged in", "outcome": "Good start! Always check the basics first.", "score": 2},
            {"text": "Immediately order a new computer", "outcome": "That's a bit hasty. Try troubleshooting first.", "score": 0},
            {"text": "Ignore the problem", "outcome": "That's not helpful. IT support is about solving problems.", "score": 0}
        ]
    },
    {
        "situation": "You notice unauthorized access attempts in the system logs. What do you do?",
        "options": [
            {"text": "Report it to the security team immediately", "outcome": "Excellent! Quick reporting is crucial for security.", "score": 2},
            {"text": "Investigate it yourself without telling anyone", "outcome": "It's better to report first to the proper channels.", "score": 1},
            {"text": "Ignore it, it's probably nothing", "outcome": "This could lead to serious security issues.", "score": 0}
        ]
    },
    {
        "situation": "A new software update is available for the company's main application. How do you proceed?",
        "options": [
            {"text": "Install it immediately on all systems", "outcome": "It's better to test updates before wide deployment.", "score": 1},
            {"text": "Test it on a non-production system first", "outcome": "Great approach! Always test before deploying.", "score": 2},
            {"text": "Ignore the update", "outcome": "Updates often contain important security patches.", "score": 0}
        ]
    },
    {
        "situation": "An employee reports that their computer is running very slowly. What's your first step?",
        "options": [
            {"text": "Check for recent software updates or installations", "outcome": "Good thinking! Recent changes can often cause performance issues.", "score": 2},
            {"text": "Immediately format the hard drive", "outcome": "That's a drastic step that could lead to data loss. Always try less invasive solutions first.", "score": 0},
            {"text": "Ignore the complaint", "outcome": "Ignoring user complaints can lead to decreased productivity and frustration.", "score": 0}
        ]
    },
    {
        "situation": "You need to implement a new software system company-wide. How do you proceed?",
        "options": [
            {"text": "Roll it out to everyone at once without testing", "outcome": "This could lead to widespread issues if there are any problems with the software.", "score": 0},
            {"text": "Conduct a pilot test with a small group before full implementation", "outcome": "Excellent! This allows you to identify and resolve issues before they affect the entire company.", "score": 2},
            {"text": "Ask each department to implement it themselves", "outcome": "This could lead to inconsistencies and support difficulties across the organization.", "score": 1}
        ]
    }
]

# Team Lead Bingo Facts
TEAM_LEAD_FACTS = [
    "Set clear goals", "Provide regular feedback", "Encourage collaboration",
    "Recognize achievements", "Promote work-life balance", "Conduct team meetings",
    "Resolve conflicts", "Delegate tasks", "Mentor team members",
    "Plan project timelines", "Assess team performance", "Implement agile methodologies",
    "Foster innovation", "Manage resources", "Ensure clear communication",
    "Define team roles", "Set priorities", "Manage stakeholder expectations",
    "Encourage skill development", "Lead by example", "Promote diversity and inclusion",
    "Handle crisis situations", "Celebrate team successes", "Align team with company vision"
]

# Spielobjekte
GAME_OBJECTS = [
    {"name": "Company Handbook", "description": "Contains important company policies.", "sprite": "chest", "position": (200, 200)},
    {"name": "Coffee", "description": "A productivity booster!", "sprite": "potion", "position": (400, 400)},
    {"name": "Laptop", "description": "Your work computer.", "sprite": "chest", "position": (600, 100)},
    {"name": "ID Badge", "description": "Your company identification.", "sprite": "chest", "position": (150, 450)}
]

# Spielwelt-Konfiguration
WORLD_CONFIG = {
    "map_size": (1000, 1000),
    "obstacle_positions": [
        (50, 50, 50, 50),  # x, y, width, height
        (150, 150, 50, 50),
        (300, 300, 100, 20),
        (400, 400, 20, 100),
    ]
}

# Spieler-Starteinstellungen
PLAYER_INITIAL_CONFIG = {
    "position": (400, 300),
    "speed": 5,
    "initial_level": 1,
    "xp_per_level": 100
}

# Weitere Spielinhalte können hier hinzugefügt werden

# Charaktere
CHARACTERS = {
    "player": {
        "name": "New Employee",
        "sprite": "player",
        "initial_position": (400, 300),
        "speed": 5,
        "initial_level": 1,
        "xp_per_level": 100
    }
}

# NPCs
NPCS = {
    "HR Manager": {
        "name": "Sarah",
        "position": (100, 100),
        "sprite": "npc_hr_manager",
        "dialogue": "Welcome! I'm Sarah from HR. Let's discuss our company culture."
    },
    "IT Specialist": {
        "name": "Mike",
        "position": (300, 200),
        "sprite": "npc_it_specialist",
        "dialogue": "Hi there! I'm Mike from IT. Need help with your tech setup?"
    },
    "Team Lead": {
        "name": "Emily",
        "position": (500, 300),
        "sprite": "npc_team_lead",
        "dialogue": "Hello! I'm Emily, your Team Lead. Let's talk about your role and responsibilities."
    }
}

# NPC Dialoge
NPC_DIALOGUES = {
    "HR Manager": {
        "greeting": "Welcome to our company! I'm Sarah from HR. How can I assist you today?",
        "options": [
            {
                "text": "Tell me about the company culture",
                "response": "Our culture is built on innovation, collaboration, and continuous learning. We value diversity and encourage open communication at all levels.",
                "follow_up": [
                    {"text": "How do you promote diversity?", "response": "We have various initiatives, including diversity training, inclusive hiring practices, and employee resource groups."},
                    {"text": "What learning opportunities are available?", "response": "We offer regular workshops, online courses, and a mentorship program to support continuous learning."}
                ]
            },
            {
                "text": "What are the key policies I should know?",
                "response": "The most important policies are outlined in our employee handbook. They cover topics like work hours, leave policies, and our code of conduct.",
                "follow_up": [
                    {"text": "Can you tell me more about the leave policy?", "response": "We offer a competitive leave package, including paid time off, sick leave, and parental leave. The details are in the handbook."},
                    {"text": "What's the dress code?", "response": "We have a business casual dress code. The specifics are outlined in the employee handbook."}
                ]
            },
            {
                "text": "How does the onboarding process work?",
                "response": "Our onboarding process is designed to get you up to speed quickly. It includes orientation sessions, training modules, and meetings with key team members.",
                "follow_up": [
                    {"text": "How long does onboarding typically last?", "response": "The initial onboarding usually takes about two weeks, but we see it as an ongoing process throughout your first few months."},
                    {"text": "Will I have a mentor?", "response": "Yes, we assign each new employee a mentor to help guide them through their first few months."}
                ]
            },
            {"text": "I'm ready for a challenge", "response": "Great! Let's test your knowledge about HR policies and practices.", "start_game": True}
        ]
    },
    "IT Specialist": {
        "greeting": "Hi there! I'm Mike from IT. How can I help you with your tech needs?",
        "options": [
            {
                "text": "What IT resources are available to me?",
                "response": "We provide a suite of productivity tools, including email, project management software, and collaboration platforms. I can help you set these up.",
                "follow_up": [
                    {"text": "How do I access the project management tool?", "response": "You can find the login credentials in the IT resources section of our intranet."},
                    {"text": "What's the password for the collaboration platform?", "response": "Please don't share passwords. You can reset your password using the 'Forgot Password' option."}
                ]
            },
            {
                "text": "How do I report IT issues?",
                "response": "You can submit a ticket through our internal help desk system. For urgent issues, you can reach out to our IT support hotline.",
                "follow_up": [
                    {"text": "What's the IT support hotline number?", "response": "The IT support hotline number is 555-1234."},
                    {"text": "Can I call outside of business hours?", "response": "No, the IT support hotline is available during business hours only."}
                ]
            },
            {
                "text": "Tell me about our cybersecurity practices",
                "response": "We take cybersecurity seriously. We have regular training sessions and use state-of-the-art security measures to protect our systems and data.",
                "follow_up": [
                    {"text": "What kind of training do we offer?", "response": "We offer cybersecurity awareness training, phishing simulations, and incident response exercises."},
                    {"text": "What's our policy on password security?", "response": "We require strong passwords with a combination of uppercase letters, lowercase letters, numbers, and special characters."}
                ]
            },
            {"text": "I'd like to test my IT problem-solving skills", "response": "Excellent! Let's go through some common IT scenarios.", "start_game": True}
        ]
    },
    "Team Lead": {
        "greeting": "Hello! I'm Emily, your Team Lead. What would you like to know about our team and projects?",
        "options": [
            {
                "text": "What's our team structure like?",
                "response": "Our team operates in an agile framework. We have daily stand-ups, sprint planning sessions, and regular retrospectives to continuously improve our processes.",
                "follow_up": [
                    {"text": "Who's the Scrum Master?", "response": "Our Scrum Master is Jane. She facilitates our agile processes and ensures we follow the framework."},
                    {"text": "What's the role of the Product Owner?", "response": "The Product Owner is responsible for defining and prioritizing the product backlog, representing stakeholder needs, and making decisions."}
                ]
            },
            {
                "text": "What kind of projects will I be working on?",
                "response": "You'll be involved in a variety of projects, ranging from internal tools development to client-facing applications. We always aim to match projects with team members' skills and interests.",
                "follow_up": [
                    {"text": "How do I request a new project?", "response": "You can submit a project request through the project management tool on our intranet."},
                    {"text": "What's the process for selecting projects?", "response": "Projects are selected based on strategic alignment, feasibility, and team capacity."}
                ]
            },
            {
                "text": "How do you handle team conflicts?",
                "response": "We encourage open communication and try to address conflicts early. If needed, we facilitate mediation sessions to ensure a positive team environment.",
                "follow_up": [
                    {"text": "What's the mediation process like?", "response": "Mediation sessions are confidential and facilitated by a neutral third party. They help parties understand each other's perspectives and find a resolution."},
                    {"text": "What if mediation doesn't work?", "response": "In rare cases, if mediation fails, we may involve HR for further intervention."}
                ]
            },
            {"text": "I'm interested in leadership challenges", "response": "That's great to hear! Let's go through some leadership scenarios to hone your skills.", "start_game": True}
        ]
    },
    "Coworker": {
        "greeting": "Hey there! I'm a fellow coworker. How's your day going?",
        "options": [
            {
                "text": "How long have you been working here?",
                "response": "I've been with the company for about 2 years now. It's been a great experience so far!",
                "follow_up": [
                    {"text": "What's your favorite part about working here?", "response": "I really enjoy the collaborative atmosphere and the opportunities for growth."},
                    {"text": "Have you worked on any interesting projects?", "response": "Yes, I've been involved in several exciting projects. The most recent one was developing a new feature for our main product."}
                ]
            },
            {
                "text": "Do you have any tips for a new employee?",
                "response": "Absolutely! Don't be afraid to ask questions, take advantage of the learning resources, and try to connect with people from different departments.",
                "follow_up": [
                    {"text": "Are there any specific resources you'd recommend?", "response": "The company's online learning platform is great, and our weekly tech talks are really informative."},
                    {"text": "How can I connect with people from other departments?", "response": "Join some of the company's social clubs or attend the monthly all-hands meetings. They're a lot of fun!"}
                ]
            },
            {
                "text": "What's the work culture like here?",
                "response": "It's pretty great! We have a good balance of professionalism and fun. The company really values work-life balance and employee well-being.",
                "follow_up": [
                    {"text": "Are there any team-building activities?", "response": "Yes, we have quarterly team outings and regular social events. They're a lot of fun!"},
                    {"text": "How does the company support work-life balance?", "response": "We have flexible working hours, remote work options, and generous time-off policies."}
                ]
            },
            {"text": "Thanks for the chat!", "response": "No problem at all! Feel free to come chat anytime you need help or just want to talk.", "start_game": False}
        ]
    }
}

# Spielobjekte
GAME_OBJECTS = [
    {"name": "Company Handbook", "description": "Contains important company policies.", "sprite": "chest", "position": (200, 200)},
    {"name": "Coffee", "description": "A productivity booster!", "sprite": "potion", "position": (400, 400)},
    {"name": "Laptop", "description": "Your work computer.", "sprite": "chest", "position": (600, 100)},
    {"name": "ID Badge", "description": "Your company identification.", "sprite": "chest", "position": (150, 450)}
]

# Spielwelt-Konfiguration
WORLD_CONFIG = {
    "map_size": (1000, 1000),
    "obstacle_positions": [
        (50, 50, 50, 50),  # x, y, width, height
        (150, 150, 50, 50),
        (300, 300, 100, 20),
        (400, 400, 20, 100),
    ]
}

# Spieler-Starteinstellungen
PLAYER_INITIAL_CONFIG = {
    "position": (400, 300),
    "speed": 5,
    "initial_level": 1,
    "xp_per_level": 100
}

# Weitere Spielinhalte können hier hinzugefügt werden

# Team Leadership Scenario
TEAM_LEAD_SCENARIOS = [
    {
        "situation": "A team member is consistently missing deadlines. How do you address this?",
        "options": [
            {"text": "Have a private conversation to understand the underlying issues", "score": 3, "feedback": "Great choice! Open communication helps identify and solve problems."},
            {"text": "Immediately report them to HR", "score": 1, "feedback": "This might be too harsh without first trying to resolve the issue directly."},
            {"text": "Ignore the problem and hope it resolves itself", "score": 0, "feedback": "Ignoring issues often leads to bigger problems down the line."}
        ]
    },
    {
        "situation": "Your team is struggling with a new project methodology. What's your approach?",
        "options": [
            {"text": "Organize a team training session", "score": 3, "feedback": "Excellent! This addresses the issue while promoting team learning."},
            {"text": "Switch back to the old methodology immediately", "score": 1, "feedback": "This might solve the immediate problem but doesn't help the team grow."},
            {"text": "Tell the team to figure it out on their own", "score": 0, "feedback": "As a leader, it's important to provide guidance and support."}
        ]
    },
    {
        "situation": "There's conflict between two team members affecting the whole team. How do you handle it?",
        "options": [
            {"text": "Mediate a discussion between them to find a resolution", "score": 3, "feedback": "Great approach! This addresses the issue directly and promotes understanding."},
            {"text": "Separate them and assign them to different projects", "score": 1, "feedback": "This might solve the immediate issue but doesn't address the underlying problem."},
            {"text": "Tell them to keep their personal issues out of work", "score": 0, "feedback": "This dismisses the impact on the team and doesn't solve the problem."}
        ]
    },
    {
        "situation": "Your team has successfully completed a major project. How do you celebrate?",
        "options": [
            {"text": "Organize a team outing or party", "score": 3, "feedback": "Excellent! This builds team morale and acknowledges their hard work."},
            {"text": "Give a brief 'good job' in the next team meeting", "score": 1, "feedback": "While positive, this might not fully acknowledge the team's efforts."},
            {"text": "Do nothing, completing projects is expected", "score": 0, "feedback": "Celebrating successes is important for team morale and motivation."}
        ]
    },
    {
        "situation": "A team member approaches you with an innovative idea. How do you respond?",
        "options": [
            {"text": "Listen carefully and help develop the idea further", "score": 3, "feedback": "Great! This encourages innovation and makes team members feel valued."},
            {"text": "Tell them to focus on their current tasks instead", "score": 1, "feedback": "This might maintain short-term productivity but stifles innovation and motivation."},
            {"text": "Dismiss the idea without consideration", "score": 0, "feedback": "This discourages creativity and can make team members feel undervalued."}
        ]
    }
]

# Fortschrittssystem
ONBOARDING_PROGRESS = {
    "Company Culture": {"max_score": 10, "description": "Understanding of company values and practices"},
    "HR Policies": {"max_score": 10, "description": "Knowledge of key company policies"},
    "IT Systems": {"max_score": 10, "description": "Proficiency in using company IT systems"},
    "Team Dynamics": {"max_score": 10, "description": "Understanding of team structure and collaboration"},
    "Job Responsibilities": {"max_score": 10, "description": "Clarity on role and responsibilities"}
}

# Belohnungen für Minispiele
MINIGAME_REWARDS = {
    "HR Quiz": {"xp": 50, "item": "Employee Handbook Pro"},
    "IT Scenarios": {"xp": 50, "item": "Cybersecurity Badge"},
    "Leadership Challenge": {"xp": 50, "item": "Team Leader Certificate"}
}

# Interaktive Objekte in der Spielwelt
INTERACTIVE_OBJECTS = [
    {
        "name": "Information Kiosk",
        "position": (150, 150),
        "sprite": "kiosk",
        "interaction": "Provides company information and FAQs",
        "knowledge_gain": {"Company Culture": 1}
    },
    {
        "name": "Training Terminal",
        "position": (450, 450),
        "sprite": "terminal",
        "interaction": "Offers quick training modules on various topics",
        "knowledge_gain": {"IT Systems": 1, "Job Responsibilities": 1}
    },
    {
        "name": "Meeting Room",
        "position": (700, 200),
        "sprite": "meeting_room",
        "interaction": "A place for team discussions and presentations",
        "knowledge_gain": {"Team Dynamics": 1}
    }
]

import random
from content.game_config import get_npc_distribution, LEVEL_CONFIGS, LEVELS

def generate_npcs(level):
    npc_distribution = get_npc_distribution(level)
    npcs = []
    for role, count in npc_distribution.items():
        for i in range(count):
            npc = {
                "name": f"{role}_{i+1}",
                "role": role,
                "position": (random.randint(50, 950), random.randint(50, 950)),
                "sprite": f"npc_{role.lower().replace(' ', '_')}",
                "dialogue": NPC_DIALOGUES.get(role, {}).get("greeting", f"Hello, I'm a {role}.")
            }
            npcs.append(npc)
    return npcs

def generate_level_content(level):
    return {
        "npcs": generate_npcs(level),
        "objects": GAME_OBJECTS,
        "available_areas": LEVEL_CONFIGS[level]["available_areas"],
        "difficulty": LEVEL_CONFIGS[level]["difficulty"],
        "obstacle_positions": WORLD_CONFIG["obstacle_positions"]
    }

ALL_LEVELS_CONTENT = {level: generate_level_content(level) for level in range(1, LEVELS + 1)}