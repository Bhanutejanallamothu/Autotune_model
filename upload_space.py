from huggingface_hub import HfApi

api = HfApi()

api.upload_large_folder(
    folder_path=".",
    repo_id="bhanuteja110/autotune-api",
    repo_type="space"
)

print("Upload completed")
