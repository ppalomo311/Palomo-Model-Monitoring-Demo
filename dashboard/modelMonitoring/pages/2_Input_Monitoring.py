# view sentence length distrobution, with classification colour coding
import streamlit as st

st.logo(
    image = 'https://www.morganstanley.com/etc.clientlibs/msdotcomr4/clientlibs/clientlib-site/resources/img/logo-black.png',
    icon_image=None
)

st.title(":chart_with_upwards_trend: Input Monitoring Dashboard")


from cognition_datalab.evaluations import get_workflows
from modelMonitoring.src.utils import get_sentence_lengths
import plotly.figure_factory as ff


@st.cache_data()
def plot_sentence_length():
    # Get all workflow sentence lengths
    workflows = get_workflows()

    sentence_lengths = []
    for workflow in workflows:
        sentence_lengths.append(get_sentence_lengths(workflow))

    # Display sentence length distribution
    hist_data = [x['sentence_length'] for x in sentence_lengths]
    group_labels = [x['workflow_id'] for x in sentence_lengths]

    fig = ff.create_distplot(hist_data, group_labels, bin_size=0.5)
    fig.update_layout(
        title="Sentence Length Distribution",
        xaxis_title="Sentence Length",
        yaxis_title="Frequency",
        legend_title="Workflow ID",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )

    return fig

plot = plot_sentence_length()

st.plotly_chart(plot)
