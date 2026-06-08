> **OBSOLETE / ARCHIVED — See [docs/GOALOS_DOCUMENTATION_INDEX.md](docs/GOALOS_DOCUMENTATION_INDEX.md) and [docs/GOALOS_WEBSITE_AUTONOMOUS_ACTIONS.md](docs/GOALOS_WEBSITE_AUTONOMOUS_ACTIONS.md).** This legacy web-upload guide is retained for historical context only. Current public-site changes must go through autonomous GitHub Actions, must use the v14 validation path, and must not upload paid buyer products.

# GitHub web upload checklist

Use this as a simple checklist while uploading.

- [ ] Repository is under `MontrealAI`
- [ ] Repository is named exactly `skillos`
- [ ] Repository is public
- [ ] Uploaded the contents of `UPLOAD_THE_CONTENTS_OF_THIS_FOLDER_TO_GITHUB`
- [ ] Did not upload only the ZIP file
- [ ] Did not upload the wrapper folder itself
- [ ] `.github/workflows/pages.yml` exists
- [ ] `.github/workflows/tests.yml` exists
- [ ] `site/index.html` exists
- [ ] `scripts/build_pages.py` exists
- [ ] `scripts/verify_repo.py` exists
- [ ] Settings → Pages → Source is `GitHub Actions`
- [ ] Actions → `Deploy SkillOS website to GitHub Pages` is green
- [ ] Live URL opens: `https://montrealai.github.io/proof-gradient/`
