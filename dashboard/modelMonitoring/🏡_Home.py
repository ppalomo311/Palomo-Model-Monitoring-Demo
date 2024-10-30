import streamlit as st


st.logo(
    image = 'https://www.morganstanley.com/etc.clientlibs/msdotcomr4/clientlibs/clientlib-site/resources/img/logo-black.png',
    icon_image=None
)

st.title('🏡 Compliance Model Monitoring')

st.markdown(
    '''

    ## Cognition datalabs API endpoints  

    The following three endpoints were used to create this dashboard application.  
    
    1. ### Available evaluation workflows in cognition
    
    __Request__  
    ```python
    GET cognition/datalab/workflows
    ```

    __Library view__
    ```python
    from cognition_datalab.evaluations import get_workflows
    workflows = get_workflows()
    ```

    __Response Data__  
    ```python
    ["{workflow_id}", "{workflow_id}", ...]
    ```  
    
    2. ### Metadata for a specific evaluation workflow  

    __Request__
    ```python
    GET cognition/datalab/workflows/{workflow_id}?meta
    ``` 

    __Library view__
    ```python
    from cognition_datalab.evaluations import get_workflows, get_workflow_metadata
    workflows = get_workflows()
    workflow_metadata = get_workflow_metadata(workflows[0])
    ``` 

    __Response Data__  
    ```python
    {
        "workflow": {workflow_id},
        "communication-count": {number of communications},
        "date-run": "{date}"
    }
    ```  

    3. ### Classification results for a specific evaluation workflow  

    __Request__  
    ```python
    GET cognition/datalab/workflows/{workflow_id}/results?page={page}
    ```  

    __Library view__
    ```python
    from cognition_datalab.evaluations import get_workflows, get_workflow_results
    workflows = get_workflows()
    workflow_classifications = get_workflow_results(workflows[0])
    ```

    __Response Data__  
    ```python
    {
        'meta': {
            'workflow': 'Q1-evaluation',
            'communications': 56785,
            'date': '2023-04-01'
        },
        'classifiers': [
            {
                'id': 1, 
                'name': 'MODEL:smarsh-secrecy-en:secrecy-en-lr:1.2.0', 
                'labels': ['secrecy', 'no']
            }
        ],
        'communications': [
            {
                'messageId': 0,
                'features': [
                    {
                        'recordIdentifier': '0.0',
                        'sentence': 'can you please furnish me with your full postal address so that i can send you a copy of the garp brochure in the near future ',
                        'classifiers': [
                            {
                                'id': '1',
                                'confidence': [0.8384429738447999, 0.1615570261552001]
                            }
                        ]
                    }, {...}
                ]
            }
        ]
    }
    '''
)