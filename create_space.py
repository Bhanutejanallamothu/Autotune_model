from huggingface_hub import HfApi

api = HfApi()

api.create_repo(
    repo_id="bhanuteja110/autotune-api",
    repo_type="space",
    space_sdk="docker",
    exist_ok=True
)

print("Space ready")
