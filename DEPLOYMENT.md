# GitHub Pages Deployment

## 目标

将 RPA Spec 部署到 `https://happyfulltech.github.io/rpa-spec/`

## 配置步骤

### 1. 创建 Personal Access Token (PAT)

在 arthurdev000 账号创建 PAT：

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 设置：
   - Note: `RPA Spec Deploy`
   - Expiration: 选择合适的过期时间
   - Select scopes: 勾选 `repo` (Full control of private repositories)
4. 点击 "Generate token"
5. **立即复制 token**（只显示一次）

### 2. 在 rpa-spec 仓库添加 Secret

1. 访问 https://github.com/arthurdev000/rpa-spec/settings/secrets/actions
2. 点击 "New repository secret"
3. 设置：
   - Name: `DEPLOY_TOKEN`
   - Secret: 粘贴刚才复制的 PAT
4. 点击 "Add secret"

### 3. 推送触发部署

```bash
git add .github/workflows/deploy.yml doc/_templates doc/_static doc/conf.py
git commit -m "Add GitHub Pages deployment"
git push
```

### 4. 验证部署

- GitHub Actions 会自动运行
- 部署完成后访问：
  - HTML: https://happyfulltech.github.io/rpa-spec/
  - PDF: https://happyfulltech.github.io/rpa-spec/rpa-spec.pdf

## 文件说明

```
rpa-spec/
├── .github/workflows/deploy.yml   # GitHub Actions 配置
├── doc/
│   ├── _templates/layout.html     # 自定义模板（PDF 按钮）
│   └── _static/custom.css         # 自定义样式
└── ...
```

## 本地预览

```bash
cd /home/dev/git/academic/papers/rpa-architecture/rpa-spec
source .venv/bin/activate
sphinx-build -M html doc _build
# 打开 _build/html/index.html
```
