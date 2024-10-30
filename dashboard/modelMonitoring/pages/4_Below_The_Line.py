# plot model confidence score distrobutions
import streamlit as st

st.logo(
    image = 'https://www.morganstanley.com/etc.clientlibs/msdotcomr4/clientlibs/clientlib-site/resources/img/logo-black.png',
    icon_image=None
)

st.title(":chart_with_upwards_trend: Below The Line Investigator")

from cognition_datalab.evaluations import get_workflows
from modelMonitoring.src.utils import get_confidence_scores_with_sentences
import plotly.express as px

# Create a dropdown selection for workflows
workflows = get_workflows()

col1, col2, col3 = st.columns(3)
with col1:
    selected_workflow = st.selectbox("Select Workflow", workflows)
with col2:
    selected_threshold = st.slider("Select Threshold", 0.0, 1.0, 0.7)
with col3:
    selected_range = st.slider("Select probability range of interest", 0.0, 1.0, (selected_threshold - 0.15, selected_threshold + 0.15))


@st.cache_data()
def plot_scatter_scores(selected_workflow, selected_threshold, selected_range):
    
    df = get_confidence_scores_with_sentences(selected_workflow)
    df = df[(df.confidence_score >= selected_range[0]) & (df.confidence_score <= selected_range[1])]
    df["x"] = [i for i in range(df.shape[0])]

    fig = px.scatter(
        df,
        y="confidence_score",
        x="x",
        hover_data = {
            "x": False,
            "sentence": True
        }
    )
    fig.add_hline(y=selected_threshold, line_dash="dash", line_color="red")
    fig.update_layout(
        title="Below the Threshold Investigation",
        xaxis_title="Sample Index",
        yaxis_title="Positive Class Confidence Score",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )

    return fig

plot = plot_scatter_scores(selected_workflow, selected_threshold, selected_range)
st.plotly_chart(plot)
