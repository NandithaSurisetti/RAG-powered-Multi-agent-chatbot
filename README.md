# RAG-Powered Multi-Agent Q&A Assistant

This project implements a Retrieval-Augmented Generation (RAG) powered multi-agent system for answering user queries. The system combines tools like Wikipedia search, LangSmith documentation retriever, and a calculator to provide accurate and contextually relevant responses. It is built using LangChain and deployed using Streamlit for an interactive web interface.

---

## Features

1. **Multi-Agent Tool Orchestration**:
   - Combines multiple tools (Wikipedia search, LangSmith documentation retriever, and a Calculator).
   - Automatically selects the appropriate tool based on the query context.

2. **Retrieval-Augmented Generation**:
   - Retrieves relevant documents from LangSmith documentation using a vector database.
   - Uses Wikipedia for additional external knowledge retrieval.
   - Performs mathematical calculations using a Python AST-based REPL tool.

3. **LLM Integration**:
   - Leverages OpenAI's GPT-3.5-turbo for natural language understanding and answer generation.
   - Framework orchestrates tool usage with LangChain.

4. **Interactive Web Interface**:
   - Provides a Streamlit-based interface for user queries.
   - Displays the final answer, the tool used, and any retrieved documents (if applicable).

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- OpenAI API Key

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/NandithaSurisetti/RAG-powered-Multi-agent-chatbot.git
   cd RAG-powered-Multi-agent-chatbot
   ```

2. **Install Dependencies**:
   Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the project root directory.
   - Add your OpenAI API key in the following format:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

4. **Run the Application**:
   ```bash
   streamlit run main.py
   ```

---

## Usage

1. **Start the Streamlit App**:
   - Open the Streamlit app in your browser.
   - Enter your query in the input box.

2. **Supported Query Types**:
   - **LangSmith-related queries**:
     - Example: "What is LangSmith?"
     - The system will use the LangSmith documentation retriever and provide relevant documents.
   - **Mathematical calculations**:
     - Example: "Calculate 45 * 23."
     - The system will use the calculator tool to provide the result.
   - **General knowledge queries**:
     - Example: "What is the capital of France?"
     - The system will use the Wikipedia tool to fetch the answer.

3. **Output**:
   - The app displays:
     - The final answer.
     - The tool used.
     - Retrieved documents (if applicable, for LangSmith queries).

---

## Architecture Overview

### Tools Used
1. **Wikipedia Tool**:
   - Uses `WikipediaAPIWrapper` to retrieve top articles.
   - Integrated via `WikipediaQueryRun` for seamless interaction.

2. **LangSmith Documentation Retriever**:
   - Loads LangSmith documentation from the website.
   - Splits documents into chunks using `RecursiveCharacterTextSplitter`.
   - Utilizes `Chroma` as a vector store with `OpenAIEmbeddings` for retrieval.

3. **Calculator Tool**:
   - Uses `PythonAstREPLTool` to perform mathematical calculations safely.

### Workflow
- The LangChain agent orchestrates the tools.
- Queries are routed to the appropriate tool based on their content.
- The system generates responses using OpenAI GPT-3.5-turbo.

---

## File Structure

```
├── main.py                   # Main application file
├── requirements.txt         # List of dependencies
├── .env                     # Environment variables (OpenAI API Key)
├── README.md                # Documentation
```

---

## Example Queries

1. **LangSmith Query**:
   - **Input**: "What is LangSmith?"
   - **Output**:
     - Answer about LangSmith.
     - Retrieved documents from LangSmith documentation.

2. **Mathematical Calculation**:
   - **Input**: "Calculate 12 + 8."
   - **Output**: "20" (via the calculator tool).

3. **General Knowledge Query**:
   - **Input**: "Who is Albert Einstein?"
   - **Output**: A summary fetched from Wikipedia.

---

## Troubleshooting

1. **No OpenAI API Key**:
   - Ensure you have added your OpenAI API key to the `.env` file.

2. **Dependencies Not Installed**:
   - Run `pip install -r requirements.txt` to install all dependencies.

3. **Streamlit Not Found**:
   - Install Streamlit using:
     ```bash
     pip install streamlit
     ```

4. **Error in LangSmith Retriever**:
   - Ensure the LangSmith documentation URL (`https://docs.smith.langchain.com/`) is accessible.

---

## Future Enhancements

- Add more tools for expanded functionality (e.g., ArXiv for research papers, advanced calculators, etc.).
- Improve tool selection logic for edge cases.
- Enhance the user interface for better experience.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request.
