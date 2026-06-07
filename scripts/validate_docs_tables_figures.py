#!/usr/bin/env python3
from pathlib import Path
import csv, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
cat=yaml.safe_load((ROOT/'docs/data/goalos_catalog.yml').read_text(encoding='utf-8'))
required_docs=['docs/GOALOS_REPO_AUDIT.md','docs/GOALOS_DOCUMENTATION_INDEX.md','docs/GOALOS_COMMERCIALIZATION_STATUS.md','docs/GOALOS_PUBLIC_SITE_RELEASE_V10.md','docs/GOALOS_RECURSIVE_WORKFLOW_OS.md','docs/GOALOS_CLOUD_MVP_0_2.md','docs/GOALOS_RSI_SPRINT_WORKSHOP_PUBLIC_POSITIONING.md','docs/GOALOS_PUBLIC_SITE_ASSET_SYSTEM.md','docs/GOALOS_PAID_ARTIFACT_POLICY.md','docs/GOALOS_CLAIMS_AND_SAFE_BOUNDARY.md','docs/GOALOS_LEGAL_PAYMENTS_BUYER_SUCCESS_SUMMARY.md','docs/GOALOS_COMMUNICATIONS_FIRM_SUMMARY.md','docs/GOALOS_ENGINEERING_ROADMAP.md']
required_tables=['docs/tables/goalos_product_ladder.csv','docs/tables/goalos_offer_status.csv','docs/tables/goalos_claim_boundaries.csv','docs/tables/goalos_public_site_pages.csv','docs/tables/goalos_paid_file_policy.csv','docs/tables/goalos_aep_standards.csv','docs/tables/goalos_document_inventory.csv','docs/tables/goalos_asset_manifest.csv']
figs=['goalos_recursive_workflow_loop','goalos_product_ladder','goalos_public_site_architecture','goalos_cloud_mvp_architecture','goalos_proof_graph_concept','goalos_enterprise_safety_boundary']
errors=[]
for p in required_docs+required_tables: 
    if not (ROOT/p).exists(): errors.append(f'Missing {p}')
for f in figs:
    if not (ROOT/f'docs/figures/{f}.mmd').exists(): errors.append(f'Missing figure source {f}.mmd')
    if not (ROOT/f'docs/figures/{f}.svg').exists(): errors.append(f'Missing figure svg {f}.svg')
readme=(ROOT/'README.md').read_text(encoding='utf-8')
for p in required_docs[:5]:
    if p not in readme and Path(p).name not in readme: errors.append(f'README does not link/reference {p}')
rows=list(csv.DictReader((ROOT/'docs/tables/goalos_product_ladder.csv').read_text(encoding='utf-8').splitlines()))
for item in cat['product_ladder']:
    if not any(r['name']==item['name'] and r['price']==item['price'] and r['version']==item['version'] for r in rows): errors.append(f'Product ladder table mismatch for {item["name"]}')
for item in cat['product_ladder']:
    if not (ROOT/'site/products'/item['slug']/'index.html').exists(): errors.append(f'Missing required product page {item["slug"]}')
if cat['safe_boundary_en'] not in readme: errors.append('Required safe-boundary language missing from README')
if errors:
    print('Docs/tables/figures validation failed:'); print('\n'.join('- '+e for e in errors)); sys.exit(1)
print('✅ GoalOS docs, tables, figures, README references, pages, and safe boundary validate.')
