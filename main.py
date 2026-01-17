import os
from huggingface_hub import snapshot_download

model_sources = [
    {
        "repo_id": "black-forest-labs/FLUX.1-dev",
        "allow_patterns":[
            "flux1-dev.safetensors",
            "ae.safetensors"
        ]
    },
    {
        "repo_id": "comfyanonymous/flux_text_encoders",
        "allow_patterns":[
            "clip_l.safetensors",
            "t5xxl_fp16.safetensors"
        ]
    }
]

print(f"开始下载模型文件...")

os.makedirs("./models", exist_ok=True)
for model_source in model_sources:
    snapshot_download(
        local_dir="/root/autodl-tmp/models/",
        **model_source
    )

print("下载完成！")