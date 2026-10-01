print("--- Cloud Challenge 1 Initialized: GitHub Webhook Stream 🔄 ---")

def process_github_webhook_event(webhook_payload):
    print(f"Intercepted push event from repository: {webhook_payload.get('repo_name')}")
    
    branch = webhook_payload.get('branch', 'main')
    commit_count = webhook_payload.get('commits_pushed', 1)
    
    try:
        if branch == 'main' or branch == 'master':
            if commit_count > 0:
                print("Webhook Log: Production branch update detected.")
                return "trigger automated cloud build and secure server deployment"
            else:
                print("Webhook Notice: Empty push event received.")
                return "no action required for empty commit"
        else:
            print("Webhook Status: Development branch activity logged.")
            return "run staging unit tests and isolation checks"
            
    except Exception as err:
        print(f"Webhook Error Caught: Failed to parse event payload -> {err}")
        return "webhook payload exception handled safely"

mock_webhook_data = {"repo_name": "rabia-ai-architecture-hub", "branch": "main", "commits_pushed": 4}
print("\nRunning Cloud Test 1:")
print(process_github_webhook_event(mock_webhook_data))
