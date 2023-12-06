import pandas as pd
import json

def lambda_handler(event, context):
    try:
        # Check if the 'data' field exists in the event
        if 'data' in event:
            # Load the JSON data from the 'data' field
            data = json.loads(event['data'])
            
            # Create a Pandas DataFrame from the JSON data
            df = pd.DataFrame(data)
            
            # Perform some data processing using Pandas
            # For example, let's sum the 'value' column
            total_sum = df['value'].sum()
            
            # Return the result
            result = {
                "total_sum": total_sum
            }
            
            return {
                'statusCode': 200,
                'body': json.dumps(result)
            }
        else:
            return {
                'statusCode': 400,
                'body': "Missing 'data' field in the event."
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"An error occurred: {str(e)}"
        }

