import pandas as pd
import streamlit as st

st.set_page_config(page_title="Harmonizing Success: A Data-Driven Approach to Expanding Dilaw's Reach and Impact")

#  Function that loads the data from a CSV file into a Pandas DataFrame
def load_data():
    data = pd.read_csv("./data/mainstay_opmd_tracks.csv")
    return data

# Function that provides an overview of the project
def introduction():
    st.image("./assets/title.png")
    st.image("./assets/dilaw.jpg")
    st.subheader(
        """
        **Dilaw** is a rising indie-alternative OPM rock band from Baguio, which consists of  6 members.

        The band is famous for the track *Uhaw (Tayong Lahat)* which rose to the Philippine top charts earlier this year.

        On Spotify, the group currently has 74,537 followers and 4,631,454 monthly listeners.
        """
    )

    st.subheader("Research Objectives: How to make Dilaw a mainstay artist?")
    st.image("./assets/objectives.png")
    

# Function that explores the visualizations of key findings 
def data_viz():
    st.title("Exploratory Data Analysis")
    st.image("./assets/eda-dominate.png")
    st.image("./assets/eda-outperform.png")
    st.image("./assets/eda-75.png")
    st.image("./assets/eda-viral.png")
    st.image("./assets/eda-mainstay.png")


# Function that defines the methodology used in the project
def methodology():
    st.image("./assets/collab.png")
    st.markdown(
        """
        To improve Dilaw's position in the chart and attract new listeners, one of our research objectives is to explore potential collaborators. 

        Research shows that collaboration through hybrid songs, which is combining the genres of the collaborators, could significantly expand audience reach.
        """)

    st.image("./assets/collab1.png")
    st.markdown("By selecting collaborators based on the nearest audio features to *Uhaw (Tayong Lahat)*, we can ensure that the collaboration produces music that resonates well with Dilaw's existing fanbase. Furthermore, collaborating with artists who share similar musical styles with Dilaw can help expand its audience reach.")

    st.subheader("Machine Learning Data Pipeline")
    st.image("./assets/pipeline.png")
    st.markdown(
        """
        For the training, the input data is the top playlists that have the nearest sound and distant sounds to Dilaw's songs.  By including genres that have a similar sound to Dilaw's music, such as rock and indie rock, we are able to capture the unique features and nuances of Dilaw's music style. On the other hand, including distant genres such as soul and pop can help to broaden the scope of the training data and provide a more diverse set of examples for the model to learn from. This can help the model avoid bias towards a narrow range of genres and increase the accuracy of recommendations for listeners who may have different musical preferences.

        To validate the correctness of the model, it was tested on the recommender pool of OPM mainstay tracks. 

        Our recommender pool consists of artists that have shown consistent popularity and engagement from listeners over an extended period of time. This is important because it indicates that these artists have a dedicated fan base and are able to capture and retain the attention of a significant number of listeners. 

        Feature scaling was also applied to the test data. The output is the classification of genre tag per track which was used for the recommender engine along with the seed track of *Uhaw (Tayong Lahat)* where the recommender engine predicted genre probabilities and audio features to identify the OPM artists with the nearest sound to Dilaw.
        """
    )

    data = load_data()
    with st.expander("Data: Mainstay OPM Tracks"):
        st.dataframe(data)
        st.caption("*Source: Spotify Philippines Top 200 Charts*")


# Function to display the recommended collaborators in a Spotify playlist
def modeling():
    st.title("Potential Collaborators")
    st.markdown("The results of the recommender engine suggest that the band  should consider collaborating with **Hale**, **Moonstar88**, **SUD**, **Zack Tabudlo**, **Moira dela Torre**, and **Ben&Ben**.")
    html = '''
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/1MuEm0Wof4NLb24PaqaYzF?utm_source=generator&theme=0" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    '''
    st.components.v1.html(html, width=800, height=400)


# Function to define the summary and conlusion
def conclusion():
    st.title("How to make Dilaw a mainstay artist?")

    # Conclusion 1
    st.subheader("Diversifying Music Features")
    st.markdown(
        """
        After using **exploratory data analysis**, it is recommended for Dilaw to:
        * Stick to their sound features and music styles
        * Explore releasing tracks with similar audio features as mainstays
        """
    )

    # Conclusion 2
    st.subheader("Expanding audience reach through collaboration")
    st.markdown(
        """
        Based on the **random forest algorithm** with an accuracy of **60%**, the recommender engine suggests that the band should consider collaborating with 
        """
    )
    st.image('./assets/collab2.png')

    # Conclusion 3
    st.subheader("Providing strategic release dates")
    st.markdown(
        """
        Preferred  album release based on **time series analytics** of competitors' total monthly releases and success after track release:
        **January**, **April**  &  **September**
        """
    )

    st.subheader("Recommendation: Exploring cross-media promotions")
    st.markdown(
        """
        The track *Uhaw (Tayong Lahat)* rose to fame because of a TikTok trend. By exploring cross-media promotions, Dilaw can increase exposure to a wider range of audience and increase fan engagement through social media platforms.
        """
    )

    st.image('./assets/message.png')


# Meet the team
def the_team():
    st.title("The Team")
    st.markdown(
        """
        We are the team **Three-Beats**! We are a group of individuals from diverse backgrounds who came together as part of the Eskwelabs Data Science Cohort 11. In our third sprint, we collaborated to create a data-driven presentation on recommender engines entitled **Harmonizing Success: A Data-Driven Approach to Expanding Dilaw's Reach and Impact**. Our goals are to (1) support Dilaw in producing more hit songs that can achieve the same level of success as "Uhaw (Tayong Lahat); (2) help Dilaw identify and collaborate with artists who share a similar musical style; and (3) optimize the release dates for Dilaw's future tracks to maximize exposure and audience engagement.

        The project uses data from the Spotify Philippines Top 200 chart, filtered to get mainstay OPM tracks, which is wrangled and analyzed using Python Pandas, exploratory data analysis using Matplotlib, and machine learning algorithm using KNN, SVM and RF. Recommender engines were also utilized to provide personalized recommendation for potential collaborators.
        """
    )
    st.header("Members")
    st.subheader("[Mark Cristian Angelo Salvador](https://www.linkedin.com/in/mark-cristian-angelo-salvador-413609260/)")
    st.markdown(
        """
        * Led the charge in the overall analysis and presentation of results, ensuring that our findings were clearly and persuasively communicated to our audience.
        * Conducted exploratory data analysis on the audio features of the Spotify tracks to ensure that our findings are reliable and actionable for the client.
        * Deployed a playlist to Spotify based on the results of the recommender engine that shows the potential collaborators for the client.
        """
    )

    st.subheader("[Quenie Alaton](https://www.linkedin.com/in/quenie-alaton/)")
    st.markdown(
        """
        * Performed  time series analysis to identify the competitors' total monthly releases and success after track release to define the client's strategy for their music's release dates. 
        * Produced informative data visualizations showcasing the relationship of mainstay tracks versus Dilaw tracks.
        * Led the creation and design of an engaging slide presentation to effectively communicate our findings.
        """
    )

    st.subheader("[Justin Louise Neypes](https://www.linkedin.com/in/jlrnrph/)")
    st.markdown(
        """
        * Spearheaded the design and deployment of the Sprint 3 project on Streamlit, showcasing our findings to others.
        * Utilized machine learning modeling techniques including Random Forest, Support Vector Machines, and K Neighbors to develop a multiclass genre classification for the mainstay OPM tracks.
        * Developed a recommender engine to predict genre probabilities and audio features to identify the OPM artists with the nearest sound to Dilaw.
        """
    )

    st.subheader("Mentor: Ron Flores")

# Define the main menu
list_of_pages = [
    "Introduction",
    "Exploratory Data Analysis",
    "Data Pipeline",
    "Recommender Engine",
    "Conclusion",
    "The Team"
]

st.sidebar.title(':scroll: Main Menu')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Introduction":
    introduction()

elif selection == "Exploratory Data Analysis":
    data_viz()

elif selection == "Data Pipeline":
    methodology()

elif selection == "Recommender Engine":
    modeling()

elif selection == "Conclusion":
    conclusion()

elif selection == "The Team":
    the_team()
