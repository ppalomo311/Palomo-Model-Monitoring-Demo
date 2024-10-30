# plot model confidence score distrobutions
import streamlit as st

st.logo(
    image = 'https://www.morganstanley.com/etc.clientlibs/msdotcomr4/clientlibs/clientlib-site/resources/img/logo-black.png',
    icon_image=None
)

st.title(":chart_with_upwards_trend: Model Monitoring Dashboard")

from cognition_datalab.evaluations import get_workflows
from modelMonitoring.src.utils import get_confidence_scores
import plotly.figure_factory as ff


@st.cache_data()
def plot_confidence_scores():
    # Get all workflow sentence lengths
    workflows = get_workflows()

    scores = []
    for workflow in workflows:
        scores.append(get_confidence_scores(workflow))

    # Display sentence length distribution
    hist_data = [x for x in scores]

    fig = ff.create_distplot(hist_data, workflows, show_hist=False, show_rug=False)
    fig.update_layout(
        title="Confidence Score Distribution",
        xaxis_title="Positive Class Confidence Score",
        yaxis_title="Frequency",
        legend_title="Workflow ID",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )

    return fig

plot = plot_confidence_scores()
st.plotly_chart(plot)