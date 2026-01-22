from huggingface_hub import upload_folder

upload_folder(
    folder_path=".",
    repo_id="bhanuteja110/autotune-api",
    repo_type="space"
)
