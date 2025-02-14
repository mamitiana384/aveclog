import streamlit as st

# Initialize authentication status in session state if it doesn't exist
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None

# Check authentication and display the appropriate content
if st.session_state["authenticated"]:
    import pages.app7  # Import app7 as a module
    pages.app7.app()  # Call the main function of app7
else:
    import pages.login  # Import login as a module
    pages.login.login_page() # Call the login function

# Add a logout button (important!)
if st.session_state["authenticated"]:
    if st.button("Logout"):
        st.session_state["authenticated"] = False
        st.session_state["username"] = None
        st.experimental_rerun() # Force re-run to update the view
