import streamlit as st
import google.generativeai as genai

# Configure Gemini API
API_KEY = "AIzaSyA-9-lTQTWdNM43YdOXMQwGKDy0SrMwo6c"  # Replace with your API key
genai.configure(api_key=API_KEY)
gemini_model = genai.GenerativeModel('gemini-1.5-flash')

# Complete Delhi Metro Data
metro_data = {
    'Red Line (1)': [
        'Shaheed Sthal', 'Hindon', 'Arthala', 'Mohan Nagar', 'Shyam Park', 'Major Mohit Sharma',
        'Raj Bagh', 'Shaheed Nagar', 'Dilshad Garden', 'Jhil Mil', 'Mansarovar Park', 'Shahdara',
        'Welcome', 'Seelampur', 'Shastri Park', 'Kashmere Gate', 'Tis Hazari', 'Pul Bangash',
        'Pratap Nagar', 'Shastri Nagar', 'Inder Lok', 'Kanhaiya Nagar', 'Keshav Puram',
        'Netaji Subhash Place', 'Kohat Enclave', 'Pitam Pura', 'Rohini East', 'Rohini West', 'Rithala'
    ],
    'Yellow Line (2)': [
        'Samaypur Badli', 'Rohini Sector 18-19', 'Haiderpur Badli Mor', 'Jahangirpuri',
        'Adarsh Nagar', 'Azadpur', 'Model Town', 'GTB Nagar', 'Vishwavidyalaya', 'Vidhan Sabha',
        'Civil Lines', 'Kashmere Gate', 'Chandni Chowk', 'Chawri Bazar', 'New Delhi',
        'Rajiv Chowk', 'Central Secretariat', 'Udyog Bhawan', 'Lok Kalyan Marg', 'Jorbagh',
        'INA', 'AIIMS', 'Green Park', 'Hauz Khas', 'Malviya Nagar', 'Saket', 'Qutab Minar',
        'Chhattarpur', 'Sultanpur', 'Ghitorni', 'Arjan Garh', 'Guru Dronacharya', 'Sikanderpur',
        'MG Road', 'IFFCO Chowk', 'Huda City Centre'
    ],
    'Blue Line (3)': [
        'Dwarka Sector 21', '8–14', 'Dwarka', 'Dwarka Mor', 'Nawada', 'Uttam Nagar West',
        'Uttam Nagar East', 'Janak Puri West', 'Janak Puri East', 'Tilak Nagar', 'Subhash Nagar',
        'Tagore Garden', 'Rajouri Garden', 'Ramesh Nagar', 'Moti Nagar', 'Kirti Nagar',
        'Shadipur', 'Patel Nagar', 'Rajendra Place', 'Karol Bagh', 'Jhandewalan', 'RK Ashram Marg',
        'Rajiv Chowk', 'Barakhamba', 'Mandi House', 'Pragati Maidan', 'Indraprastha', 'Yamuna Bank',
        'Akshardham', 'Mayur Vihar Phase 1', 'Mayur Vihar Extension', 'New Ashok Nagar',
        'Noida Sector 15', 'Noida Sector 16', 'Noida Sector 18', 'Botanical Garden', 'Golf Course',
        'Noida City Centre', 'Noida Sector 34', 'Noida Sector 52', 'Noida Sector 61',
        'Noida Sector 59', 'Noida Sector 62', 'Noida Electronic City'
    ],
    'Blue Line (4)': [
        'Vaishali', 'Kaushambi', 'Anand Vihar ISBT', 'Karkardooma', 'Preet Vihar',
        'Nirman Vihar', 'Laxmi Nagar'
    ],
    'Green Line (5)': [
        'Inder Lok', 'Kirti Nagar', 'Satguru Ram Singh Marg', 'Ashok Park Main', 'Punjabi Bagh',
        'Punjabi Bagh West', 'Shivaji Park', 'Madi Pur', 'Paschim Vihar East', 'Paschim Vihar West',
        'Peera Garhi', 'Udyog Nagar', 'Surajmal Stadium', 'Nangloi', 'Nangloi Rly Station',
        'Rajdhani Park', 'Mundka', 'Mundka Industrial Area', 'Ghevra', 'Tikri Kalan',
        'Tikri Border', 'Pt. Shree Ram Sharma', 'Bahadurgarh City', 'Brig Hoshiar Singh'
    ],
    'Violet Line (6)': [
        'Kashmere Gate', 'Lal Quila', 'Jama Masjid', 'Delhi Gate', 'ITO', 'Mandi House',
        'Janpath', 'Central Secretariat', 'Khan Market', 'Jawaharlal Nehru Stadium', 'Jangpura',
        'Lajpat Nagar', 'Moolchand', 'Kailash Colony', 'Nehru Place', 'Kalkaji Mandir',
        'Govind Puri', 'Okhla', 'Jasola', 'Sarita Vihar', 'Mohan Estate', 'Tughlakabad', 'Badarpur',
        'Sarai', 'NHPC Chowk', 'Mewala Maharajpur', 'Sector 28 (Faridabad)', 'Badkal Mor',
        'Old Faridabad', 'Neelam Chowk', 'Bata Chowk', 'Escorts Mujesar', 'Sant Surdas',
        'Raja Nahar Singh'
    ],
    'Pink Line (7)': [
        'Majlis Park', 'Azadpur', 'Shalimar Bagh', 'Netaji Subhash Place', 'Shakurpur',
        'Punjabi Bagh West', 'ESI Hospital', 'Rajouri Garden', 'Maya Puri', 'Naraina Vihar',
        'Delhi Cantt', 'Durgabai Deshmukh', 'Sir Vishweshwaraya', 'Bhikaji Cama', 'Sarojini Nagar',
        'INA', 'South Extension', 'Lajpat Nagar', 'Vinobapuri', 'Ashram', 'Hazrat Nizamuddin',
        'Mayur Vihar Phase 1', 'Pocket 1', 'Trilokpuri', 'Vinod Nagar East', 'Mandawali',
        'IP Extension', 'Anand Vihar', 'Karkardooma', 'Karkarduma Court', 'Krishna Nagar',
        'East Azad Nagar', 'Welcome', 'Jaffrabad', 'Maujpur', 'Gokulpuri', 'Johri Enclave',
        'Shiv Vihar'
    ],
    'Magenta Line (8)': [
        'Janak Puri West', 'Dabri Mor', 'Dashrath Puri', 'Palam', 'Sadar Bazaar',
        'Terminal 1 IGI Airport', 'Shankar Vihar', 'Vasant Vihar', 'Munirka', 'RK Puram',
        'IIT Delhi', 'Hauz Khas', 'Panchsheel Park', 'Chirag Delhi', 'Greater Kailash',
        'Nehru Enclave', 'Kalkaji Mandir', 'Okhla NSIC', 'Sukhdev Vihar', 'Jamia Millia Islamia',
        'Okhla Vihar', 'Jasola Vihar', 'Kalindi Kunj', 'Okhla Bird Sanctuary', 'Botanical Garden'
    ],
    'Grey Line (9)': [
        'Dwarka', 'Nangli', 'Najafgarh', 'Dhansa Bus Stand'
    ],
    'Airport Express': [
        'New Delhi', 'Shivaji Stadium', 'Dhaula Kuan', 'Delhi Aero City', 'IGI Airport',
        'Dwarka Sector 21'
    ],
    'Rapid Metro Gurgaon (RGML)': [
        'Sector 55-56', '54 Chowk', '53-54', '42-43', 'Phase 1', 'Sikanderpur', 'Phase 2',
        'Belvedere Towers', 'Cyber City', 'Moulsari Avenue', 'Phase 3'
    ],
    'Aqua Line (AEL)': [
        'Noida Sector 51', 'Noida Sector 50', 'Noida Sector 76', 'Noida Sector 101',
        'Noida Sector 81', 'NSEZ', 'Noida Sector 83', 'Noida Sector 137', 'Noida Sector 142',
        'Noida Sector 143', 'Noida Sector 144', 'Noida Sector 145', 'Noida Sector 146',
        'Noida Sector 147', 'Noida Sector 148', 'Knowledge Park II', 'Pari Chowk', 'Alpha 1',
        'Delta', 'GNIDA Office', 'Depot'
    ]
}

def get_all_stations():
    """Get sorted list of all unique stations"""
    stations = list(set([station for line in metro_data.values() for station in line]))
    return sorted(stations)

def get_route_response(source, destination):
    """Get route response from Gemini"""
    prompt = f"""You are an expert Delhi Metro route planner. Use this metro network data:
    {metro_data}
    
    Plan the most efficient route from {source} to {destination}. Include:
    1. Starting line and station
    2. Transfer stations (if any) with line changes
    3. Final line and destination station
    4. Total number of stations and approximate travel time
    5. Any important landmarks or interchanges
    
    Format the response with:
    - Clear numbered steps
    - Line names in bold
    - Emojis for key points
    - Separators between main sections
    - Estimated time in minutes
    - Total stations count
    
    Make it easy to read with proper formatting using markdown."""

    response = gemini_model.generate_content(prompt)
    return response.text

# Streamlit UI Configuration
st.set_page_config(page_title="Delhi Metro Navigator", page_icon="🚇", layout="wide")

# App Interface
st.title("Delhi Metro Route Planner 🚇")
st.markdown("### AI-Powered Metro Navigation for Delhi NCR")

# Get sorted list of stations
all_stations = get_all_stations()

# Station Selection
col1, col2 = st.columns(2)
with col1:
    source = st.selectbox(
        "Starting Station:",
        options=all_stations,
        index=all_stations.index('Kashmere Gate') if 'Kashmere Gate' in all_stations else 0,
        help="Select your starting station"
    )
with col2:
    destination = st.selectbox(
        "Destination Station:",
        options=[s for s in all_stations if s != source],
        index=0,
        help="Select your destination station"
    )

# Route Planning
if st.button("Plan My Journey", type="primary", use_container_width=True):
    if source == destination:
        st.error("🚨 Source and Destination cannot be the same! Please select different stations.")
    else:
        with st.spinner("🚀 Finding optimal route..."):
            try:
                result = get_route_response(source, destination)
                st.success("🎉 Here's Your Optimal Route:")
                st.markdown("---")
                st.markdown(result, unsafe_allow_html=True)
                st.markdown("---")
                st.balloons()
            except Exception as e:
                st.error(f"⚠️ Error generating route: {str(e)}")

# Sidebar Information
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    **Delhi Metro Navigator** helps you:
    - Find optimal routes across 12 metro lines
    - Discover transfer points and travel times
    - Navigate 390+ km network efficiently
    """)
    
    st.markdown("---")
    st.subheader("🚇 Metro Lines Supported")
    st.markdown("""
    - Red Line
    - Yellow Line
    - Blue Line
    - Green Line
    - Violet Line
    - Pink Line
    - Magenta Line
    - Grey Line
    - Airport Express
    - Rapid Metro
    - Aqua Line""")
    
    st.markdown("---")
    st.warning("""
    **Important Notes:**
    - Always verify with official DMRC sources
    - Allow 5-10 minutes for transfers
    - Station names are case-insensitive
    - First/last train timings may affect routes""")

# Footer
st.markdown("---")
st.caption("Powered by Google Gemini AI • Data Source: Delhi Metro Rail Corporation (DMRC) • Updated: 2024-01-01")
