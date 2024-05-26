import streamlit as st
import pandas as pd
import seaborn as sns

@st.cache_resource
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = pd.read_csv(url)
    return df

def main():
    st.title("Iris Datensatz")
    st.write("Eine einfache Streamlit app um den Iris-Datensatz zu untersuchen.")

    df = load_data()

    # Slider for filtering by sepal length
    sepal_length_min = df['sepal_length'].min()
    sepal_length_max = df['sepal_length'].max()
    
    sepal_length_filter = st.slider(
        'Nach Kelchblattlänge filtern',
        sepal_length_min,
        sepal_length_max,
        (sepal_length_min, sepal_length_max)
    )

    filtered_df = df[
        (df['sepal_length'] >= sepal_length_filter[0]) &
        (df['sepal_length'] <= sepal_length_filter[1])
    ]

    st.subheader(f"Zeige Resultate nur für Kelchblattlänge zwischen {sepal_length_filter}")
    st.write(filtered_df.describe())

    if st.checkbox("Zeige rohe Daten"):
        st.subheader("Filtered Raw Data")
        st.write(filtered_df)

    st.subheader("Pairplot")
    st.write("Ein Pairplot zur Visualisierung der Beziehungen zwischen den Variablen.")
    fig = sns.pairplot(filtered_df, hue="species")
    st.pyplot(fig)

if __name__ == "__main__":
    main()
