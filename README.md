### Mem0 Assignment 🚀
This project demonstrates the integration and practical usage of Mem0 for building persistent memory-aware AI agents.
It showcases how user preferences, context, and historical interactions can be stored, retrieved, and reused to enhance personalized agent responses.

### 🎯 Objectives

-Understand Mem0 memory concepts and architecture
-Implement persistent memory storage for AI agents
-Store and retrieve user preferences, context, and history
-Integrate Mem0 with LLM-based agents
-Build memory-driven personalized interactions

### 🛠️ Technologies Used

-Python 3.10+
-Mem0
-LangChain (optional integration)
-GenAI / LLM APIs
-dotenv

### ⚙️ Setup Instructions

1️⃣ Clone the Repository

    git clone <repository-url>
    cd MEM0_ASSIGNMENT

2️⃣ Create Virtual Environment

    python -m venv venv
    source venv/bin/activate   # Linux / Mac
    venv\Scripts\activate      # Windows

3️⃣ Install Dependencies

    pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file:

    MEM0_API_KEY=your_mem0_api_key_here
    OPENAI_API_KEY=your_openai_api_key_here

### ▶️ Running the Project
python main.py
This will initialize the memory-enabled agent, store user interactions, and retrieve relevant memories dynamically during conversations.

### 🧠 Memory System Overview
-Memory Creation
-Stores user preferences, facts, and behavioral patterns
-Examples:
 -Preferred date format
 -Location
 -Communication style
 -Problem-solving preferences

-Memory Retrieval
 -Searches stored memories using semantic queries
 -Injects relevant context into agent responses
 -Ensures continuity across sessions

-Memory Update
 -Updates existing memories when preferences change
 -Prevents duplication and stale information

### 🤖 Agent Capabilities
-Remembers user-specific details across conversations
-Personalizes responses using stored memory
-Combines short-term context with long-term memory
-Works independently or alongside LangChain agents

### 🔐 Security Notes
-API keys are never hard-coded
-.env is added to .gitignore
-Memory access is scoped using user_id
-Sensitive data storage is avoided

### 📌 Learning Outcomes
-Strong understanding of Mem0 memory lifecycle
-Building persistent, context-aware AI agents
-Designing memory-trigger strategies
-Improving user experience with personalization
-Clean and modular memory architecture