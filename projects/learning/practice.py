# Practice workspace - Modern AI News Generator
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="AI News Generator", page_icon="📰", layout="wide")

# Title and description
st.title("🤖 AI News Generator - Modern Edition")
st.markdown("Generate comprehensive blog posts about any topic using modern AI technology.")

# Sidebar
with st.sidebar:
    st.header("Content Settings")
    
    # Make the text input take up more space
    topic = st.text_area(
        "Enter your topic",
        height=100,
        placeholder="Enter the topic you want to generate content about..."
    )
    
    # Add more sidebar controls if needed
    st.markdown("### Advanced Settings")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    
    # Add some spacing
    st.markdown("---")
    
    # Make the generate button more prominent in the sidebar
    generate_button = st.button("Generate Content", type="primary", use_container_width=True)
    
    # Add some helpful information
    with st.expander("ℹ️ How to use"):
        st.markdown("""
        1. Enter your desired topic in the text area above
        2. Adjust the temperature if needed (higher = more creative)
        3. Click 'Generate Content' to start
        4. Wait for the AI to generate your article
        5. Copy or download the result as needed
        """)

def generate_content(topic, temperature):
    """Generate comprehensive blog content using modern LangChain API"""
    
    # Initialize ChatOpenAI with modern API
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=temperature,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Research prompt template
    research_prompt = ChatPromptTemplate.from_template("""You are an expert research analyst. 
Your task is to conduct comprehensive research on: {topic}

Provide:
1. Recent developments and news
2. Key industry trends and innovations
3. Expert opinions and analyses
4. Statistical data and market insights
5. Source citations where applicable

Format your response with clear sections and bullet points.""")
    
    # Content writing prompt template
    content_prompt = ChatPromptTemplate.from_template("""You are a skilled content writer.
Based on this research about '{topic}':

{research_content}

Create an engaging, well-structured blog post that:
1. Has an attention-grabbing introduction
2. Includes well-structured body sections with clear headings
3. Maintains all factual accuracy
4. Has a compelling conclusion
5. Includes a References section at the end

Format in proper markdown with H1 for title and H3 for sub-sections.""")
    
    # Generate research content
    research_chain = research_prompt | llm
    research_result = research_chain.invoke({"topic": topic})
    research_text = research_result.content if hasattr(research_result, 'content') else str(research_result)
    
    # Generate blog post
    content_chain = content_prompt | llm
    content_result = content_chain.invoke({
        "topic": topic,
        "research_content": research_text
    })
    final_content = content_result.content if hasattr(content_result, 'content') else str(content_result)
    
    return final_content

# Main content area
if generate_button:
    if not topic.strip():
        st.error("Please enter a topic to generate content.")
    else:
        with st.spinner('Generating content... This may take a moment.'):
            try:
                result = generate_content(topic, temperature)
                
                st.success("✅ Content generated successfully!")
                st.markdown("---")
                st.markdown("## 📄 Generated Article")
                st.markdown(result)
                
                # Download button
                st.download_button(
                    label="📥 Download as Markdown",
                    data=result,
                    file_name=f"article_{topic.replace(' ', '_')}.md",
                    mime="text/markdown"
                )
                
            except Exception as e:
                st.error(f"❌ Error generating content: {str(e)}")
                st.info("Make sure your OPENAI_API_KEY environment variable is set.")
else:
    st.info("👈 Enter a topic in the sidebar and click 'Generate Content' to begin!")
            st.markdown("### Generated Content")
            st.markdown(result)
            
            # Add download button
            st.download_button(
                label="Download Content",
                data=result.raw,
                file_name=f"{topic.lower().replace(' ', '_')}_article.md",
                mime="text/markdown"
            )
        except Exception as e:

# Footer
st.markdown("---")
st.markdown("🚀 Built with Modern LangChain, Streamlit, and OpenAI GPT-4o-mini")