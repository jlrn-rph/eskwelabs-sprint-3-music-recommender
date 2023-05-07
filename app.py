import pandas as pd
import streamlit as st

st.set_page_config(page_title='Dilaw')

#  Function that loads the data from a CSV file into a Pandas DataFrame
# def load_data():
#     data = pd.read_csv(
#         "./data/mainstay_opmd_tracks.csv",
#         encoding='ISO-8859-1'
#     )
#     return data

# Function that provides an overview of the project, including research objectives, scope, and limitations
# It also displays visualizations of key metrics and displays the dataset
def introduction():
    st.title("Introduction")
    # st.image("./assets/")

    # st.markdown(
    #     """
    #     """
    # )

    # data = load_data()
    # with st.expander("View Data"):
    #     st.dataframe(data)
    #     st.caption("*Source: Spotify*")
    # )

# Function that explores the relationship between age, income, education, and financial inclusion 
# among genders in the Philippines. It provides visualizations of key findings and interprets the results
def data_viz():
    st.title("Exploratory Data Analysis")
    # st.markdown(
    #     """
    #     """
    # )


# Function to identify profiles of women who are underserved and not financially included
def modeling():
    st.title("Recommender Engine")
    # st.subheader("")
    # st.image("./assets/")
    # st.markdown(
    #     """
    #     """
    # )

# Function to define the summary and conlusion
def conclusion():
    st.title("Summary and Conclusion")

    # Conclusion 1
    # st.subheader(""")
    # st.markdown(
    #     """
    #     """
    # )

    # st.image('./assets/message.png')

# Meet the team
def the_team():
    st.title("The Team")
    st.markdown(
        """
        We are the team **Three-Beats**! We are a group of individuals from diverse backgrounds who came together as part of the Eskwelabs Data Science Cohort 11.
        """
    )
    st.header("Members")
    st.subheader("[Mark Cristian Angelo Salvador](https://www.linkedin.com/in/mark-cristian-angelo-salvador-413609260/)")
    # st.markdown(
    #     """
    #     """
    # )

    st.subheader("[Quenie Alaton](https://www.linkedin.com/in/quenie-alaton/)")
    # st.markdown(
    #     """
    #     """
    # )

    st.subheader("[Justin Louise Neypes](https://www.linkedin.com/in/jlrnrph/)")
    # st.markdown(
    #     """
    #     """
    # )

    st.subheader("Mentor: Ron Flores")

# Define the main menu
list_of_pages = [
    "Introduction",
    "Exploratory Data Analysis",
    "Modeling",
    "Conclusion",
    "The Team"
]

st.sidebar.title(':scroll: Main Menu')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Introduction":
    introduction()

elif selection == "Exploratory Data Analysis":
    data_viz()

elif selection == "Modeling":
    modeling()

elif selection == "Conclusion":
    conclusion()

elif selection == "The Team":
    the_team()
