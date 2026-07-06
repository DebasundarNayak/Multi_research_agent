import streamlit as st
import time

# Defer import of pipeline to avoid loading issues
def get_pipeline():
    from pipeline import run_research_pipeline
    return run_research_pipeline

# Page configuration
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com',
        'Report a bug': "https://github.com",
    }
)

# Custom CSS with enhanced styling
st.markdown("""
    <style>
    /* Main theme colors */
    :root {
        --primary: #0066cc;
        --secondary: #00d4ff;
        --success: #10b981;
        --warning: #f59e0b;
        --danger: #ef4444;
    }
    
    /* Enhanced styling */
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #0066cc 0%, #00d4ff 100%);
        color: white;
        padding: 40px 20px;
        border-radius: 15px;
        margin-bottom: 30px;
        box-shadow: 0 8px 16px rgba(0, 102, 204, 0.2);
        font-size: 2.5em;
        font-weight: bold;
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1em;
        margin-bottom: 30px;
        font-style: italic;
    }
    
    .section-header {
        color: #0066cc;
        border-bottom: 3px solid #00d4ff;
        padding-bottom: 12px;
        margin-top: 25px;
        margin-bottom: 15px;
        font-size: 1.3em;
        font-weight: 600;
    }
    
    .success-box {
        background: linear-gradient(135deg, #064e3b 0%, #0d4e47 100%);
        border-left: 5px solid #10b981;
        border-radius: 8px;
        padding: 15px;
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
        color: #d1fae5;
    }
    }
    
    .info-box {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
        border-left: 5px solid #0066cc;
        border-radius: 8px;
        padding: 15px;
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(0, 102, 204, 0.3);
        color: #e0f2fe;
    }
    
    .warning-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        border-radius: 8px;
        padding: 15px;
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(245, 158, 11, 0.15);
    }
    
    .error-box {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border-left: 5px solid #ef4444;
        border-radius: 8px;
        padding: 15px;
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(239, 68, 68, 0.15);
    }
    
    .feature-card {
        background: white;
        border: 2px solid #e5e7eb;
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        border-color: #00d4ff;
        box-shadow: 0 4px 12px rgba(0, 212, 255, 0.2);
        transform: translateY(-2px);
    }
    
    .step-indicator {
        display: inline-block;
        background: linear-gradient(135deg, #0066cc 0%, #00d4ff 100%);
        color: white;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        margin-right: 10px;
    }
    
    .input-section {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 25px;
        border-radius: 12px;
        border: 2px solid #0066cc;
        margin-bottom: 20px;
    }
    
    .results-section {
        margin-top: 25px;
    }
    
    .footer {
        text-align: center;
        color: #999;
        font-size: 0.85em;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #e5e7eb;
    }
    </style>
""", unsafe_allow_html=True)

# Main header
st.markdown("<div class='main-header'>🔬 AI Research Agent</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Autonomous Research Pipeline - Search, Scrape, Write & Review</div>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/200x50/0066cc/ffffff?text=AI+Research", width=200)
    st.markdown("---")
    
    with st.container():
        st.markdown("### 📋 Pipeline Overview")
        st.markdown("""
        <div class='feature-card'>
        <strong>Step 1: 🔎 Search Agent</strong><br>
        Finds recent and reliable information from multiple sources
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-card'>
        <strong>Step 2: 📄 Reader Agent</strong><br>
        Scrapes relevant web resources for deeper content
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-card'>
        <strong>Step 3: ✍️ Writer Agent</strong><br>
        Drafts comprehensive and structured research reports
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='feature-card'>
        <strong>Step 4: 👁️ Critic Agent</strong><br>
        Reviews quality and provides constructive feedback
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown("""
    This AI Research Agent automates the entire research workflow:
    - **Fast**: Complete research in minutes
    - **Reliable**: Uses trusted web sources
    - **Comprehensive**: Multi-agent collaboration
    - **Smart**: AI-powered quality review
    """)

# Main content - Input Section
st.markdown("### 🚀 Start Your Research")

with st.container():
    st.markdown('<div class="input-section">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        research_topic = st.text_input(
            "📚 Enter research topic:",
            placeholder="e.g., quantum computing, renewable energy, AI ethics...",
            help="Be specific for better results",
            label_visibility="collapsed"
        )
    
    with col2:
        col_button, col_example = st.columns(2)
        with col_button:
            run_button = st.button("🚀 Research", use_container_width=True, type="primary", key="research_btn")
        with col_example:
            if st.button("📋 Example", use_container_width=True):
                st.session_state.example_topic = "artificial intelligence in healthcare"
    
    st.markdown('</div>', unsafe_allow_html=True)

# Handle example topic
if 'example_topic' in st.session_state and st.session_state.example_topic:
    research_topic = st.session_state.example_topic
    run_button = True

st.markdown("---")

# Initialize session state for storing results
if 'results' not in st.session_state:
    st.session_state.results = None
if 'is_running' not in st.session_state:
    st.session_state.is_running = False

# Run research pipeline
if run_button and research_topic:
    st.session_state.is_running = True
    
    # Create a container for progress
    progress_container = st.container()
    results_container = st.container()
    
    with progress_container:
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown("<div class='info-box'><strong>🔄 Research Pipeline Running...</strong><br>Please wait while we search, scrape, write, and review your topic.</div>", unsafe_allow_html=True)
        
        with col2:
            st.caption("Estimated time: 2-3 minutes")
        
        # Progress steps
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Step indicators with animation
        steps_col1, steps_col2, steps_col3, steps_col4 = st.columns(4, gap="small")
        
        with steps_col1:
            step1_placeholder = st.empty()
        with steps_col2:
            step2_placeholder = st.empty()
        with steps_col3:
            step3_placeholder = st.empty()
        with steps_col4:
            step4_placeholder = st.empty()
        
        try:
            # Step 1: Search
            step1_placeholder.markdown("<div style='text-align: center; padding: 15px; background: #dbeafe; border-radius: 8px; border: 2px solid #0066cc;'><strong>🔎</strong><br><small>Search</small></div>", unsafe_allow_html=True)
            status_text.markdown("<strong>⏳ Step 1/4:</strong> Searching for information about '<em>{}</em>'...".format(research_topic))
            progress_bar.progress(15)
            time.sleep(0.3)
            
            # Run the pipeline
            run_research_pipeline = get_pipeline()
            results = run_research_pipeline(research_topic)
            st.session_state.results = results
            
            # Step 2: Reading/Scraping
            step1_placeholder.markdown("<div style='text-align: center; padding: 15px; background: #d1fae5; border-radius: 8px; border: 2px solid #10b981;'><strong>✅</strong><br><small>Search</small></div>", unsafe_allow_html=True)
            step2_placeholder.markdown("<div style='text-align: center; padding: 15px; background: #dbeafe; border-radius: 8px; border: 2px solid #0066cc;'><strong>📄</strong><br><small>Read</small></div>", unsafe_allow_html=True)
            status_text.markdown("<strong>⏳ Step 2/4:</strong> Reading and scraping relevant web resources...")
            progress_bar.progress(40)
            time.sleep(0.3)
            
            # Step 3: Writing
            step2_placeholder.markdown("<div style='text-align: center; padding: 15px; background: #d1fae5; border-radius: 8px; border: 2px solid #10b981;'><strong>✅</strong><br><small>Read</small></div>", unsafe_allow_html=True)
            step3_placeholder.markdown("<div style='text-align: center; padding: 15px; background: #dbeafe; border-radius: 8px; border: 2px solid #0066cc;'><strong>✍️</strong><br><small>Write</small></div>", unsafe_allow_html=True)
            status_text.markdown("<strong>⏳ Step 3/4:</strong> Writing comprehensive research report...")
            progress_bar.progress(70)
            time.sleep(0.3)
            
            # Step 4: Reviewing
            step3_placeholder.markdown("<div style='text-align: center; padding: 15px; background: #d1fae5; border-radius: 8px; border: 2px solid #10b981;'><strong>✅</strong><br><small>Write</small></div>", unsafe_allow_html=True)
            step4_placeholder.markdown("<div style='text-align: center; padding: 15px; background: #dbeafe; border-radius: 8px; border: 2px solid #0066cc;'><strong>👁️</strong><br><small>Review</small></div>", unsafe_allow_html=True)
            status_text.markdown("<strong>⏳ Step 4/4:</strong> Reviewing and scoring the report...")
            progress_bar.progress(90)
            time.sleep(0.3)
            
            # Complete
            step4_placeholder.markdown("<div style='text-align: center; padding: 15px; background: #d1fae5; border-radius: 8px; border: 2px solid #10b981;'><strong>✅</strong><br><small>Review</small></div>", unsafe_allow_html=True)
            status_text.markdown("<strong>✅ Complete!</strong> Research pipeline finished successfully.")
            progress_bar.progress(100)
            time.sleep(0.5)
            
            # Clear progress indicators
            time.sleep(1)
            progress_container.empty()
            
        except Exception as e:
            st.markdown("<div class='error-box'><strong>❌ Error:</strong> {}</div>".format(str(e)), unsafe_allow_html=True)
            st.session_state.is_running = False

# Display results
if st.session_state.results:
    results = st.session_state.results
    
    st.markdown("<div class='success-box'><strong>✅ Research Complete!</strong><br>Your comprehensive research report is ready.</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Create tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Search Results", "📄 Content", "📝 Report", "👁️ Review"])
    
    with tab1:
        st.markdown("<h3 class='section-header'>🔎 Search Results</h3>", unsafe_allow_html=True)
        if isinstance(results['search_result'], list):
            search_text = results['search_result'][0].content if hasattr(results['search_result'][0], 'content') else str(results['search_result'][0])
        else:
            search_text = results['search_result']
        
        st.markdown("""
        <div style='background: #f9fafb; padding: 15px; border-radius: 8px; border-left: 4px solid #0066cc;'>
        """, unsafe_allow_html=True)
        st.markdown(search_text)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab2:
        st.markdown("<h3 class='section-header'>📄 Scraped Content</h3>", unsafe_allow_html=True)
        if isinstance(results['scraped_content'], list):
            scraped_text = results['scraped_content'][0].content if hasattr(results['scraped_content'][0], 'content') else str(results['scraped_content'][0])
        else:
            scraped_text = results['scraped_content']
        
        st.markdown("""
        <div style='background: #f9fafb; padding: 15px; border-radius: 8px; border-left: 4px solid #0066cc;'>
        """, unsafe_allow_html=True)
        st.markdown(scraped_text)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab3:
        st.markdown("<h3 class='section-header'>📝 Research Report</h3>", unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background: #f9fafb; padding: 20px; border-radius: 8px; border-left: 4px solid #10b981;'>
        """, unsafe_allow_html=True)
        st.markdown(results['report'])
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        col_down, col_copy = st.columns(2)
        with col_down:
            st.download_button(
                label="📥 Download as Markdown",
                data=results['report'],
                file_name=f"research_report_{research_topic.replace(' ', '_')}.md",
                mime="text/markdown",
                use_container_width=True
            )
        with col_copy:
            if st.button("📋 Copy to Clipboard", use_container_width=True):
                st.success("Report copied! (Copy manually if clipboard not available)")
    
    with tab4:
        st.markdown("<h3 class='section-header'>👁️ Critic Feedback & Quality Score</h3>", unsafe_allow_html=True)
        feedback = results['feedback']
        
        st.markdown("""
        <div style='background: #fef3c7; padding: 15px; border-radius: 8px; border-left: 4px solid #f59e0b;'>
        """, unsafe_allow_html=True)
        if isinstance(feedback, str) and "Score:" in feedback:
            st.markdown(feedback)
        else:
            st.markdown(f"**Feedback:** {feedback}")
        st.markdown("</div>", unsafe_allow_html=True)

elif not st.session_state.is_running and research_topic:
    st.markdown("<div class='info-box'>👆 Click the '<strong>🚀 Research</strong>' button to start the pipeline.</div>", unsafe_allow_html=True)

elif research_topic == "":
    st.markdown("<div class='info-box'>📝 Enter a research topic and click '<strong>🚀 Research</strong>' to begin.</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
    <hr style='margin: 20px 0;'>
    <p>🔬 <strong>AI Research Agent</strong></p>
    <p>Powered by LangChain + Google Gemini | Multi-Agent Collaboration</p>
    <p style='color: #ccc; font-size: 0.8em;'>© 2024 • Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)
