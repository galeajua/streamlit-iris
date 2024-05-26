import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_resource
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = pd.read_csv(url)
    return df

def main():
    st.title("Iris Datensatz")
    st.write("Einfache Streamlit app um den Iris-Datensatz zu untersuchen.")

    df = load_data()

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

    st.subheader(f"Statistiken für Kelchblattlängen zwischen {sepal_length_filter}")
    st.write(filtered_df.describe())

    if st.checkbox("Zeige rohe Daten"):
        st.subheader("Gefiltert nach rohen Daten")
        st.write(filtered_df)

    st.subheader("Histogram der Kelchblattlänge")
    fig, ax = plt.subplots()
    ax.hist(filtered_df['sepal_length'], bins=20, color='skyblue', edgecolor='black')
    ax.set_xlabel('Kelchblattlänge')
    ax.set_ylabel('Häufigkeit')
    ax.set_title('Verteilung der Kelchblattlänge')
    st.pyplot(fig)

    st.subheader("Scatter Plot: Kelchblattlänge vs. Blütenblattlänge")
    fig, ax = plt.subplots()
    species_colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
    for species, color in species_colors.items():
        species_data = filtered_df[filtered_df['species'] == species]
        ax.scatter(species_data['sepal_length'], species_data['petal_length'], 
                   label=species, color=color)
    ax.set_xlabel('Kelchblattlänge')
    ax.set_ylabel('Blütenblattlänge')
    ax.set_title('Kelchblattlänge vs. Blütenblattlänge')
    ax.legend()
    st.pyplot(fig)

if __name__ == "__main__":
    main()
