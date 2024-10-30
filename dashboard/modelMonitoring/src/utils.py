from cognition_datalab.evaluations import get_workflow_results
import pandas as pd
import streamlit as st

THRESHOLD = 0.7

def is_alert(communication_features, threshold):
    """given a list of sentence classification, determine if the communication triggered an alert"""
    max_score = max([x[1] for x in [y.get("classifiers")[0].get("confidence") for y in communication_features]])
    if max_score >= threshold:
        return True
    else:
        return False
    

# comm features to flat row
@st.cache_data()
def workflow_to_dataframe(workflow_id, threshold):
    """given a workflow id, return a dataframe of all sentences with their alert status"""
    workflow_results = get_workflow_results(workflow_id)
    all_sentences = []
    for comm in workflow_results.get("communications"):
        message_id = comm.get("messageId")
        alert_status = is_alert(comm.get("features"), threshold)
        for sentence in comm.get("features"):
            all_sentences.append(
                {
                    "message_id": message_id,
                    "sentence_id": sentence.get("recordIdentifier"),
                    "alerted": alert_status, 
                    "sentence": sentence.get("sentence"),
                    "confidence_score": sentence.get("classifiers")[0].get("confidence")[1]
                }
            )
    return pd.DataFrame(all_sentences)


# Sentence Lengths
st.cache_data()
def get_sentence_lengths(workflow_id):
    df = workflow_to_dataframe(workflow_id, THRESHOLD)
    sentence_length = [len(x.split()) for x in df['sentence'].tolist()]
    sentence_length = [x for x in sentence_length if x <= 50]
    return {
        "workflow_id": workflow_id,
        "sentence_length": sentence_length[:10000]
    }

# Confidence Scores
st.cache_data()
def get_confidence_scores(workflow_id):
    df = workflow_to_dataframe(workflow_id, THRESHOLD)
    scores = df["confidence_score"].tolist()
    return  scores


# Confidence Scores
st.cache_data()
def get_confidence_scores_with_sentences(workflow_id):
    df = workflow_to_dataframe(workflow_id, THRESHOLD)
    scores_with_sentences = df[["confidence_score", "sentence"]]
    return  scores_with_sentences

# Evaluation Summaries

@st.cache_data()
def get_comm_count_metrics(all_workflow_ids, all_metadata):
    """generate metrics for communication counts"""
    comm_summaries = []
    for i, x in enumerate(all_workflow_ids):
        current_quarter = all_metadata[x]["communications"]
        if i == 0:
            comms_delta = 0
        else:
            previous_quarter = all_metadata[all_workflow_ids[i-1]]["communications"]
            comms_delta = ((current_quarter - previous_quarter)/current_quarter)*100
        comm_summaries.append(
            {
                "label": f"{x}",
                "value": f"{current_quarter:,}",
                "delta": f"{round(comms_delta):,}%"
            }
        )
    return comm_summaries


@st.cache_data()
def get_alert_count_metrics(all_workflow_ids, all_metadata):
    """generate metrics for alert counts"""
    alert_summaries = []
    for i, x in enumerate(all_workflow_ids):
        current_quarter = all_metadata[x]["Alerts"]
        if i == 0:
            alert_delta = 0
        else:
            previous_quarter = all_metadata[all_workflow_ids[i-1]]["Alerts"]
            alert_delta = ((current_quarter - previous_quarter)/current_quarter)*100
        alert_summaries.append(
            {
                "label": f"{x}",
                "value": f"{current_quarter:,}",
                "delta": f"{round(alert_delta):,}%"
            }
        )
    return alert_summaries  


@st.cache_data()
def get_alert_rate_metrics(all_workflow_ids, all_metadata):
    """generate metrics for alert rates"""
    alert_rate_summaries = []
    for i, x in enumerate(all_workflow_ids):
        current_quarter_alerts = all_metadata[x]["Alerts"]
        current_quarter_comms = all_metadata[x]["communications"]
        current_quarter_alert_rate = (current_quarter_alerts/current_quarter_comms)*100
        if i == 0:
            alert_rate_delta = 0
        else:
            previous_quarter_alerts = all_metadata[all_workflow_ids[i-1]]["Alerts"]
            previous_quarter_comms = all_metadata[all_workflow_ids[i-1]]["communications"]
            previous_quarter_alert_rate = (previous_quarter_alerts/previous_quarter_comms)*100
            alert_rate_delta = ((current_quarter_alert_rate - previous_quarter_alert_rate)/current_quarter_alert_rate)*100
        alert_rate_summaries.append(
            {
                "label": f"{x}",
                "value": f"{round(current_quarter_alert_rate):,}%",
                "delta": f"{round(alert_rate_delta):,}%"
            }
        )
    return alert_rate_summaries