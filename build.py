#!/usr/bin/env python3
"""Static site generator for the Abu Horairah Engineering Portfolio.
Reads data/projects.json and emits all HTML pages. Pure stdlib, no deps.
Run: python3 build.py
"""
import json, os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ROOT, "data", "projects.json")) as f:
    DATA = json.load(f)
PROJECTS = DATA["projects"]

SITE_NAME = "ABU HORAIRAH | ENGINEERING PORTFOLIO"
SITE_DESC = "Designing, building and optimizing AI, HPC, semiconductor EDA, enterprise networking and advanced storage infrastructure."
BASE_URL = "https://engrabuhorairah.github.io/profile"  # confirmed live GitHub Pages URL

def esc(s): return html.escape(str(s), quote=True)

def nav(active, depth=""):
    pages = [("Home", "index.html", "home"), ("About", "about.html", "about"),
             ("Projects", "projects.html", "projects"), ("Technologies", "technologies.html", "tech"),
             ("Architecture", "architecture.html", "arch"), ("Contact", "contact.html", "contact")]
    links = "\n".join(
        f'<a href="{depth}{href}" class="{"active" if key==active else ""}">{label}</a>'
        for label, href, key in pages
    )
    return f"""
<nav class="navbar">
  <div class="container">
    <a href="{depth}index.html" class="brand"><span class="mark">AH</span> ABU HORAIRAH</a>
    <div class="nav-links" id="navLinks">
      {links}
    </div>
    <div class="nav-actions">
      <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">☀️</button>
      <button class="nav-burger" id="navBurger" aria-label="Menu">☰</button>
    </div>
  </div>
</nav>"""

def footer(depth=""):
    return f"""
<footer>
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="brand" style="margin-bottom:14px;"><span class="mark">AH</span> ABU HORAIRAH</div>
        <p class="text-muted" style="max-width:360px;">Engineering intelligent computing infrastructure across AI, HPC, semiconductor EDA, enterprise networking and advanced storage.</p>
      </div>
      <div>
        <h4>Navigate</h4>
        <a href="{depth}projects.html">Projects</a>
        <a href="{depth}technologies.html">Technologies</a>
        <a href="{depth}architecture.html">Architecture</a>
        <a href="{depth}about.html">About</a>
      </div>
      <div>
        <h4>Connect</h4>
        <a href="https://github.com/EngrAbuHorairah" id="footer-github" target="_blank" rel="noopener">GitHub</a>
        <a href="https://www.linkedin.com/in/engrabuhorairahsandhu" id="footer-linkedin" target="_blank" rel="noopener">LinkedIn</a>
        <a href="mailto:engr.abuhorairahsandhu@gmail.com" id="footer-email">Email</a>
        <a href="{depth}contact.html" id="footer-contact">Contact No. +92 (302) 7966942</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Abu Horairah. All rights reserved.</span>
      <span>Built with HTML5, CSS3 &amp; JavaScript — deployed on GitHub Pages.</span>
    </div>
  </div>
</footer>"""

def page_shell(title, description, active, body, depth="", extra_head="", extra_js="", og_image=""):
    canonical = f"{BASE_URL}/{depth}{'' if active!='home' else ''}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)} | {SITE_NAME}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%22100%22 rx=%2220%22 fill=%22%230a0e17%22/><text x=%2250%22 y=%2268%22 font-size=%2258%22 text-anchor=%22middle%22 fill=%22%2322d3ee%22 font-family=%22monospace%22 font-weight=%22bold%22>AH</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{depth}assets/css/main.css">
{extra_head}
</head>
<body>
{nav(active, depth)}
{body}
{footer(depth)}
<script src="{depth}assets/js/main.js"></script>
{extra_js}
</body>
</html>"""

# ---------------------------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------------------------
def build_home():
    categories = [
        ("Artificial Intelligence", "ai", "Private AI platforms, distributed training clusters and AIOps assistants."),
        ("High-Performance Computing", "hpc", "Slurm clusters, HPC monitoring and scientific computing environments."),
        ("Electronic Design Automation", "eda", "EDA compute farms, license optimization and RTL-to-GDSII automation."),
        ("High-Performance Networking", "networking", "Data center fabrics, RDMA/InfiniBand design and Zero Trust security."),
        ("Enterprise Storage", "storage", "Distributed storage, parallel file systems and disaster recovery.")
    ]
    featured = PROJECTS[:3]
    cat_cards = "\n".join(f"""
      <a href="projects.html#{slug}" class="card">
        <h3>{name}</h3>
        <p class="text-muted" style="margin-top:10px;">{desc}</p>
      </a>""" for name, slug, desc in categories)

    featured_cards = "\n".join(f"""
      <a href="projects/{p['slug']}.html" class="card project-card">
        <span class="pnum">PROJECT {p['id']:02d}</span>
        <h3>{p['title']}</h3>
        <div class="cat">{p['category']}</div>
        <p class="desc">{p['short']}</p>
        <div class="meta-row">
          <span class="badge-status {p['statusClass']}"><span class="dot"></span>{p['status']}</span>
          <span class="view-link">View Details &rarr;</span>
        </div>
      </a>""" for p in featured)

    body = f"""
<section class="hero">
  <div class="container">
    <div class="hero-badge"><span class="dot"></span> AI / HPC / EDA / Network / Storage Engineering</div>
    <h1>Building the Infrastructure Behind <span class="gradient-text">Intelligent Computing.</span></h1>
    <p class="lead">Specializing in AI infrastructure, HPC clusters, semiconductor EDA environments, high-performance networking and enterprise storage solutions.</p>
    <div class="btn-row">
      <a href="projects.html" class="btn btn-primary">Explore Projects</a>
      <a href="technologies.html" class="btn btn-outline">Technical Expertise</a>
      <a href="contact.html" class="btn btn-ghost">Contact / Collaborate</a>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="grid grid-4">
      <div class="card" style="text-align:center;"><div class="stat-num" data-counter="14">0</div><div class="stat-label">Engineering Projects</div></div>
      <div class="card" style="text-align:center;"><div class="stat-num" data-counter="5">0</div><div class="stat-label">Infrastructure Domains</div></div>
      <div class="card" style="text-align:center;"><div class="stat-num" data-counter="40">0</div><div class="stat-label">Technologies Covered</div></div>
      <div class="card" style="text-align:center;"><div class="stat-num" data-counter="6">0</div><div class="stat-label">Roadmap Phases per Project</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow">Specialization</span>
    <h2 style="margin:14px 0 36px;">Engineering Categories</h2>
    <div class="grid grid-3">{cat_cards}</div>
  </div>
</section>

<section class="section" style="background:var(--bg-secondary);">
  <div class="container">
    <span class="eyebrow">Featured Work</span>
    <h2 style="margin:14px 0 36px;">Featured Projects</h2>
    <div class="grid grid-3">{featured_cards}</div>
    <div style="margin-top:32px;"><a href="projects.html" class="btn btn-outline">View All 14 Projects &rarr;</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow">Capability</span>
    <h2 style="margin:14px 0 36px;">Engineering Capabilities</h2>
    <div class="grid grid-4">
      <div class="card"><h3 style="font-size:1.1rem;">GPU &amp; AI Infrastructure</h3><p class="text-muted" style="margin-top:8px;font-size:0.9rem;">CUDA, distributed training, inference serving, RAG pipelines.</p></div>
      <div class="card"><h3 style="font-size:1.1rem;">HPC Systems</h3><p class="text-muted" style="margin-top:8px;font-size:0.9rem;">Slurm scheduling, MPI/OpenMP, scientific computing environments.</p></div>
      <div class="card"><h3 style="font-size:1.1rem;">EDA Infrastructure</h3><p class="text-muted" style="margin-top:8px;font-size:0.9rem;">License servers, compute farms, open-source digital design flows.</p></div>
      <div class="card"><h3 style="font-size:1.1rem;">Networking &amp; Storage</h3><p class="text-muted" style="margin-top:8px;font-size:0.9rem;">RDMA fabrics, Zero Trust security, Ceph, parallel file systems.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-box">
      <span class="eyebrow">Let's Build Something</span>
      <h2 style="margin:14px 0 18px;">Interested in developing similar infrastructure for your organization?</h2>
      <p class="lead" style="margin:0 auto 28px;">Let's discuss your technical requirements.</p>
      <a href="contact.html" class="btn btn-primary">Contact / Collaborate</a>
    </div>
  </div>
</section>
"""
    html_out = page_shell("Home", SITE_DESC, "home", body, depth="")
    write("index.html", html_out)

# ---------------------------------------------------------------------------
# ABOUT PAGE
# ---------------------------------------------------------------------------
def build_about():
    experience = [
        {"role": "IT Manager (HPC &amp; Chip Designing)", "org": "NUST Chip Design Centre", "period": "November 2025 &mdash; Present", "loc": "Islamabad, Pakistan",
         "points": [
            "Provides hands-on training to students and engineers on HPC workflows, ARM architecture, EDA deployment, Linux administration and semiconductor design infrastructure.",
            "Manages high-performance clusters optimized for ARM-based silicon design, including Slurm/LSF workloads, resource allocation, simulation scheduling and performance tuning.",
            "Administers Cadence ICADVM, Virtuoso, Spectre and ADE platforms for analog/mixed-signal IC design flows.",
            "Designed and deployed a secure, air-gapped private AI engineering platform using vLLM, Qwen3-Coder, Qdrant, BGE-M3, FastAPI and Open WebUI for AI-assisted engineering and knowledge retrieval.",
            "Implemented RBAC, audit logging, mTLS, secrets management, network isolation, monitoring, backup, disaster recovery and GPU failover for secure, resilient engineering services."
         ]},
        {"role": "AI/HPC System and Network Engineer (Dev/MLOps)", "org": "AS-Softlayer Technologies", "period": "December 2023 &mdash; September 2025", "loc": "Islamabad, Pakistan",
         "points": [
            "Designed and built a complete data center infrastructure from scratch, including virtualization with Proxmox, OpenStack and VMware ESXi.",
            "Architected and deployed the ATTOM Data Center, handling full build-out, configuration and monitoring solution implementation.",
            "Deployed NVIDIA Mellanox SN3700 switches for HA-enabled production networking (MLAG, CLAG, LACP, OSPF, VRF).",
            "Worked with NVIDIA GPUs including RTX 4090, M10, 4050 and DGX H200 servers for AI workloads and deep learning training.",
            "Deployed and managed Dell EMC ECS (2PB) and PowerScale NAS for large-scale object and file storage infrastructure."
         ]},
        {"role": "Senior HPC Support Specialist / Slurm Engineer", "org": "Redfort Technologies", "period": "February 2024 &mdash; January 2025", "loc": "United States (Remote)",
         "points": [
            "Delivered advanced support for HPC clusters, optimizing performance and managing storage systems.",
            "Configured and optimized SLURM for efficient HPC cluster management, including accounting, database and Node Health Checks (NHC).",
            "Resolved scheduling issues, enhanced resource utilization and trained team members on SLURM tools and best practices."
         ]},
        {"role": "HPC &amp; MLOps Engineer (Freelance)", "org": "NexGen IT Hub", "period": "April 2022 &mdash; February 2024", "loc": "Okara District, Punjab, Pakistan",
         "points": [
            "Designed, deployed and maintained multiple HPC clusters using Lustre, BeeGFS and NFS for compute-intensive scientific and AI workloads.",
            "Implemented SLURM, PBS and Torque job scheduling with full resource partitioning and QoS policies.",
            "Integrated real-world HPC applications: OpenFOAM, GROMACS, Abaqus, LAMMPS, NAMD, ANSYS, Gaussian, Quantum ESPRESSO.",
            "Developed MLOps pipelines using MLflow, Kubeflow, GitHub Actions and Docker for full model lifecycle management."
         ]},
        {"role": "Linux System Administrator / DevOps (Freelance)", "org": "Self-employed", "period": "February 2021 &mdash; March 2022", "loc": "Okara District, Punjab, Pakistan",
         "points": [
            "Maintained secure, stable and optimized Linux environments across Debian, Ubuntu, Rocky Linux, CentOS, Red Hat and FreeBSD.",
            "Deployed and managed VMs, containers and services on AWS (EC2, S3, VPC) and Azure.",
            "Implemented automated backup and disaster recovery strategies."
         ]},
        {"role": "Computer Science Lecturer", "org": "Johar Educational Complex", "period": "June 2021 &mdash; November 2023", "loc": "Okara District, Punjab, Pakistan",
         "points": ["Planned lessons, delivered lectures and conducted laboratory sessions in Information Technology and Computer Science."]},
        {"role": "Online HPC Instructor", "org": "Chalmers University of Technology", "period": "September 2022 &mdash; August 2023", "loc": "Sweden (Remote)",
         "points": ["Delivered virtual instruction on OpenMP, MPI, OpenCL, memory optimization and performance tuning; mentored students through parallel programming assignments."]},
    ]
    exp_html = "".join(f"""
      <div class="card" style="margin-bottom:18px;">
        <div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;">
          <h3 style="font-size:1.05rem;">{e['role']}</h3>
          <span class="text-muted" style="font-size:0.85rem;">{e['period']}</span>
        </div>
        <div class="text-muted" style="margin-bottom:10px;font-size:0.9rem;">{e['org']} &middot; {e['loc']}</div>
        <ul style="font-size:0.9rem;">{''.join(f'<li>{pt}</li>' for pt in e['points'])}</ul>
      </div>""" for e in experience)

    body = f"""
<section class="hero" style="padding-top:64px;padding-bottom:40px;">
  <div class="container">
    <span class="eyebrow">About</span>
    <h1 style="margin-top:14px;">Engineering Profile</h1>
    <p class="lead">AI/HPC Solutions Architect &amp; MLOps Consultant &mdash; EDA Tools, GPU Infrastructure, Cloud Computing, Kubernetes, Terraform, SLURM, Cadence, Xilinx, Synopsys, Enterprise Storage &amp; Networking, ARM.</p>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="card">
      <h3>Professional Introduction</h3>
      <p class="text-muted" style="margin-top:12px;">I'm Abu Horairah Sandhu, an AI/HPC Solutions Architect and MLOps Consultant based in Islamabad, Pakistan, specializing in eliminating infrastructure bottlenecks for engineering and R&amp;D teams &mdash; from chip-design EDA clusters to GPU-accelerated AI training pipelines. Over 3+ years, I've architected HPC environments integrating SLURM/PBS job scheduling, parallel file systems (BeeGFS, Lustre, Panasas), NVIDIA GPU clusters (including DGX H200 and RTX 4090), and end-to-end MLOps pipelines (Kubeflow, MLflow, PyTorch). I've also built EDA-integrated HPC infrastructure for Cadence Virtuoso and Xilinx Vivado workflows with high-availability FlexLM licensing, deployed secure air-gapped private AI platforms for internal engineering teams, and managed enterprise storage exceeding 2PB (Dell EMC ECS, PowerScale) alongside high-performance networking (InfiniBand, Mellanox). I'm open to consulting projects worldwide, remote or on-site &mdash; if your team is dealing with slow simulations, GPU underutilization, storage bottlenecks, or license contention, let's talk.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 style="margin-bottom:30px;">Technical Specializations</h2>
    <div class="grid grid-3">
      <div class="card"><h3 style="font-size:1.05rem;">HPC Cluster Design &amp; Deployment</h3><p class="text-muted" style="margin-top:8px;font-size:0.9rem;">SLURM, PBS/Torque, LSF, xCAT, Bright Cluster Manager, Node Health Checks.</p></div>
      <div class="card"><h3 style="font-size:1.05rem;">GPU &amp; AI Infrastructure</h3><p class="text-muted" style="margin-top:8px;font-size:0.9rem;">CUDA, NVIDIA DGX H200/RTX 4090 clusters, MLOps with Kubeflow/MLflow/PyTorch.</p></div>
      <div class="card"><h3 style="font-size:1.05rem;">EDA Infrastructure</h3><p class="text-muted" style="margin-top:8px;font-size:0.9rem;">Cadence (Virtuoso, Spectre, ICADVM, ADE), Xilinx Vivado, Synopsys, high-availability FlexLM licensing.</p></div>
      <div class="card"><h3 style="font-size:1.05rem;">Enterprise Storage</h3><p class="text-muted" style="margin-top:8px;font-size:0.9rem;">2PB+ Dell EMC ECS, PowerScale NAS, Lustre, BeeGFS, Panasas, NFS.</p></div>
      <div class="card"><h3 style="font-size:1.05rem;">HPC &amp; Enterprise Networking</h3><p class="text-muted" style="margin-top:8px;font-size:0.9rem;">InfiniBand, Mellanox (SN3700, MLAG/CLAG/LACP/OSPF/VRF), Cisco, Nexus, Aruba.</p></div>
      <div class="card"><h3 style="font-size:1.05rem;">Automation &amp; Monitoring</h3><p class="text-muted" style="margin-top:8px;font-size:0.9rem;">Ansible, Terraform, Kubernetes, Grafana, Prometheus, Zabbix, Netdata.</p></div>
    </div>
  </div>
</section>

<section class="section" style="background:var(--bg-secondary);">
  <div class="container">
    <h2 style="margin-bottom:30px;">Experience</h2>
    {exp_html}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2">
      <div class="card">
        <h3>Education</h3>
        <p style="margin-top:10px;"><strong>BS, Computer Science</strong><br><span class="text-muted">University of Okara &middot; November 2021 &mdash; June 2025</span></p>
        <p style="margin-top:10px;"><strong>Associate Engineer</strong><br><span class="text-muted">Punjab Board of Technical Education (PBTE), Lahore</span></p>
      </div>
      <div class="card">
        <h3>Certifications</h3>
        <ul style="margin-top:10px;">
          <li>Linux and Private Cloud Administration on IBM Power Systems (Specialization)</li>
          <li>Linux System Administration with IBM Power Systems</li>
          <li>Private Cloud Management on IBM Power Systems</li>
          <li>Cisco Industrial Networking Essentials (CINE)</li>
          <li>Computer Vision App with Azure Cognitive Services</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""
    write("about.html", page_shell("About", "Engineering profile of Abu Horairah Sandhu — AI/HPC Solutions Architect & MLOps Consultant specializing in EDA, GPU infrastructure, enterprise storage and networking.", "about", body))

# ---------------------------------------------------------------------------
# PROJECTS OVERVIEW PAGE
# ---------------------------------------------------------------------------
def build_projects_overview():
    all_tech = sorted({t for p in PROJECTS for t in p["tech"]})
    tech_options = "\n".join(f'<option value="{esc(t)}">{esc(t)}</option>' for t in all_tech)
    cards = "\n".join(f"""
      <a href="projects/{p['slug']}.html" id="{p['categorySlug']}" class="card project-card">
        <span class="pnum">PROJECT {p['id']:02d}</span>
        <h3>{p['title']}</h3>
        <div class="cat">{p['category']}</div>
        <p class="desc">{p['short']}</p>
        <div>{''.join(f'<span class="tag">{esc(t)}</span>' for t in p['tech'][:4])}</div>
        <div class="meta-row">
          <span class="badge-status {p['statusClass']}"><span class="dot"></span>{p['status']}</span>
          <span class="view-link">View Details &rarr;</span>
        </div>
      </a>""" for p in PROJECTS)

    data_js = json.dumps(PROJECTS)

    body = f"""
<section class="hero" style="padding-top:64px;padding-bottom:32px;">
  <div class="container">
    <span class="eyebrow">Portfolio</span>
    <h1 style="margin-top:14px;">14 Engineering Projects</h1>
    <p class="lead">Across AI, high-performance computing, semiconductor EDA, enterprise networking and storage infrastructure.</p>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="filter-bar">
      <input type="text" id="projectSearch" placeholder="Search projects, technologies...">
      <select id="statusFilter">
        <option value="all">All Statuses</option>
        <option value="Concept">Concept</option>
        <option value="Proposed">Proposed</option>
        <option value="In Development">In Development</option>
        <option value="Prototype">Prototype</option>
        <option value="Implemented">Implemented</option>
        <option value="Production">Production</option>
      </select>
      <select id="techFilter">
        <option value="all">All Technologies</option>
        {tech_options}
      </select>
    </div>
    <div class="filter-bar">
      <span class="chip active" data-category-filter="all">All</span>
      <span class="chip" data-category-filter="ai">Artificial Intelligence</span>
      <span class="chip" data-category-filter="hpc">High-Performance Computing</span>
      <span class="chip" data-category-filter="eda">Electronic Design Automation</span>
      <span class="chip" data-category-filter="networking">High-Performance Networking</span>
      <span class="chip" data-category-filter="storage">Enterprise Storage</span>
    </div>
    <div class="grid grid-3" id="projectGrid">
      {cards}
    </div>
  </div>
</section>
<script>
  const PROJECTS_DATA = {data_js};
  document.addEventListener('DOMContentLoaded', () => initProjectFilters(PROJECTS_DATA));
</script>
"""
    write("projects.html", page_shell("Projects", "All 14 engineering projects across AI, HPC, EDA, networking and storage.", "projects", body))

# ---------------------------------------------------------------------------
# TECHNOLOGIES PAGE
# ---------------------------------------------------------------------------
def build_technologies():
    groups = {}
    for p in PROJECTS:
        groups.setdefault(p["category"], set()).update(p["tech"])
    sections = "\n".join(f"""
      <div class="card" style="margin-bottom:24px;">
        <h3>{esc(cat)}</h3>
        <div style="margin-top:14px;">{''.join(f'<span class="tag">{esc(t)}</span>' for t in sorted(techs))}</div>
      </div>""" for cat, techs in groups.items())
    body = f"""
<section class="hero" style="padding-top:64px;padding-bottom:32px;">
  <div class="container">
    <span class="eyebrow">Expertise</span>
    <h1 style="margin-top:14px;">Technology Stack</h1>
    <p class="lead">Technologies spanning AI infrastructure, HPC, EDA, networking and storage engineering.</p>
  </div>
</section>
<section class="section-tight">
  <div class="container">{sections}</div>
</section>
"""
    write("technologies.html", page_shell("Technologies", "Technology stack across AI, HPC, EDA, networking and storage projects.", "tech", body))

# ---------------------------------------------------------------------------
# ARCHITECTURE PAGE
# ---------------------------------------------------------------------------
def build_architecture():
    body = """
<section class="hero" style="padding-top:64px;padding-bottom:32px;">
  <div class="container">
    <span class="eyebrow">Architecture</span>
    <h1 style="margin-top:14px;">Infrastructure Architecture Showcase</h1>
    <p class="lead">A high-level view of how the five engineering domains in this portfolio relate to one another.</p>
  </div>
</section>
<section class="section-tight">
  <div class="container">
    <div class="mermaid">
graph TD
  A[Enterprise Networking Fabric] --> B[HPC Compute Cluster]
  A --> C[AI Training & Inference Cluster]
  A --> D[EDA Compute Farm]
  B --> E[Parallel File System]
  C --> E
  D --> F[Distributed Storage - Ceph]
  E --> G[Backup & Disaster Recovery]
  F --> G
  B --> H[Monitoring & AIOps]
  C --> H
  D --> H
  A --> H
    </div>
    <p class="text-muted" style="margin-top:24px;">Networking (Project 10/11) underlies every compute domain. HPC and AI workloads (Projects 02, 04, 06) rely on the parallel file system (Project 13) for high-throughput I/O, while EDA (Projects 07-09) relies on the distributed storage platform (Project 12) and centralized licensing. Every domain feeds into unified monitoring/AIOps (Project 03/05) and is protected by the backup &amp; DR platform (Project 14).</p>
  </div>
</section>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.9.0/mermaid.min.js"></script>
<script>mermaid.initialize({ startOnLoad: true, theme: 'dark' });</script>
"""
    write("architecture.html", page_shell("Architecture", "How AI, HPC, EDA, networking and storage infrastructure domains interconnect.", "arch", body))

# ---------------------------------------------------------------------------
# CONTACT PAGE
# ---------------------------------------------------------------------------
def build_contact():
    body = """
<section class="hero" style="padding-top:64px;padding-bottom:40px;">
  <div class="container">
    <span class="eyebrow">Contact</span>
    <h1 style="margin-top:14px;">Let's Discuss Your Infrastructure Requirements</h1>
    <p class="lead">Interested in developing similar infrastructure for your organization? Reach out below.</p>
    <div class="grid grid-2" style="margin-top:40px;max-width:720px;">
      <div class="card"><h3 style="font-size:1rem;">GitHub</h3><p class="text-muted" style="margin-top:8px;">[YOUR_GITHUB_URL]</p></div>
      <div class="card"><h3 style="font-size:1rem;">LinkedIn</h3><p class="text-muted" style="margin-top:8px;"><a href="https://www.linkedin.com/in/engrabuhorairahsandhu" target="_blank" rel="noopener" style="color:var(--accent-cyan);">engrabuhorairahsandhu</a></p></div>
      <div class="card"><h3 style="font-size:1rem;">Email</h3><p class="text-muted" style="margin-top:8px;"><a href="mailto:engr.abuhorairahsandhu@gmail.com" style="color:var(--accent-cyan);">engr.abuhorairahsandhu@gmail.com</a></p></div>
      <div class="card"><h3 style="font-size:1rem;">Website</h3><p class="text-muted" style="margin-top:8px;">[YOUR_PERSONAL_SITE]</p></div>
    </div>
  </div>
</section>
"""
    write("contact.html", page_shell("Contact", "Get in touch to discuss AI, HPC, EDA, networking or storage infrastructure projects.", "contact", body))

# ---------------------------------------------------------------------------
# 404 PAGE
# ---------------------------------------------------------------------------
def build_404():
    body = """
<section class="hero" style="text-align:center;">
  <div class="container">
    <h1 class="gradient-text" style="font-size:5rem;">404</h1>
    <p class="lead" style="margin:0 auto 28px;">This page could not be found.</p>
    <a href="index.html" class="btn btn-primary">Return Home</a>
  </div>
</section>
"""
    write("404.html", page_shell("Page Not Found", "Page not found.", "", body))

# ---------------------------------------------------------------------------
# PROJECT DETAIL PAGES
# ---------------------------------------------------------------------------
def list_items(items):
    return "".join(f"<li>{esc(i)}</li>" for i in items)

def build_project_page(p):
    tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in p["tech"])
    stack_rows = "".join(
        f"<tr><td><strong>{esc(s['tech'])}</strong></td><td>{esc(s['why'])}</td></tr>" for s in p["stackRationale"]
    )
    roadmap_html = "".join(f"""
      <div class="roadmap-phase">
        <div class="pnum2">{i+1}</div>
        <div><strong>{esc(r['phase'])}</strong><p class="text-muted" style="margin-top:4px;font-size:0.9rem;">{esc(r['detail'])}</p></div>
      </div>""" for i, r in enumerate(p["roadmap"]))

    mermaid_arch = f"""graph LR
  U[User / Client] --> GW[Application / Gateway Layer]
  GW --> CORE[{p['title'].split('(')[0].strip()[:28]} Core Services]
  CORE --> DATA[(Data / Storage Layer)]
  CORE --> MON[Monitoring & Observability]
  MON --> ADMIN[Administrator]"""

    mermaid_flow = f"""flowchart TD
  P1[Phase 1: Planning] --> P2[Phase 2: Infrastructure Prep]
  P2 --> P3[Phase 3: Install & Configure]
  P3 --> P4[Phase 4: Integration]
  P4 --> P5[Phase 5: Testing & Benchmarking]
  P5 --> P6[Phase 6: Production Readiness]"""

    hw = p["hardware"]
    sw = p["software"]
    sec = p["security"]
    bd = p["businessDetail"]

    extra_note = f'<div class="note-box">{esc(p["note"])}</div>' if "note" in p else ""
    comparison_note = f'<div class="note-box"><strong>Technology Comparison:</strong> {esc(p["comparisonNote"])}</div>' if "comparisonNote" in p else ""
    when_to_use = f'<div class="note-box"><strong>When to use each:</strong> {esc(p["whenToUse"])}</div>' if "whenToUse" in p else ""

    body = f"""
<section class="project-hero">
  <div class="container">
    <div class="breadcrumb"><a href="../index.html">Home</a> / <a href="../projects.html">Projects</a> / {esc(p['title'])}</div>
    <span class="eyebrow">PROJECT {p['id']:02d} &middot; {esc(p['category'])}</span>
    <h1 style="margin:14px 0 16px;">{esc(p['title'])}</h1>
    <p class="lead">{esc(p['short'])}</p>
    <div style="margin:18px 0;">
      <span class="badge-status {p['statusClass']}"><span class="dot"></span>{esc(p['status'])}</span>
    </div>
    <div>{tags}</div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="grid" style="grid-template-columns: 220px 1fr; gap:40px;" id="projectLayout">
      <aside class="toc-sticky">
        <strong style="display:block;margin-bottom:8px;font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;">On this page</strong>
        <a href="#overview">Overview</a>
        <a href="#business-value">Business Value</a>
        <a href="#architecture">Architecture</a>
        <a href="#stack">Technology Stack</a>
        <a href="#hardware">Hardware</a>
        <a href="#software">Software</a>
        <a href="#roadmap">Roadmap</a>
        <a href="#security">Security &amp; Reliability</a>
        <a href="#testing">Testing &amp; Validation</a>
        <a href="#deliverables">Deliverables</a>
        <a href="#future">Future Enhancements</a>
        <a href="../projects.html">&larr; Back to Projects</a>
      </aside>

      <div>
        <div class="detail-section" id="overview">
          <h2>A. Project Overview</h2>
          <h4>Problem Statement</h4><p>{esc(p['problem'])}</p>
          <h4>Proposed Solution</h4><p>{esc(p['solution'])}</p>
          <h4>Objectives</h4><ul>{list_items(p['objectives'])}</ul>
          <h4>Intended Users</h4><p>{esc(p['users'])}</p>
          {extra_note}
        </div>

        <div class="detail-section" id="business-value">
          <h2>B. Business Value</h2>
          <table class="spec-table">
            <tr><th>Operational Benefits</th><td>{esc(bd['operational'])}</td></tr>
            <tr><th>Cost Optimization</th><td>{esc(bd['cost'])}</td></tr>
            <tr><th>Productivity</th><td>{esc(bd['productivity'])}</td></tr>
            <tr><th>Scalability</th><td>{esc(bd['scalability'])}</td></tr>
            <tr><th>Security &amp; Reliability</th><td>{esc(bd['security'])}</td></tr>
            <tr><th>Organizational Impact</th><td>{esc(bd['impact'])}</td></tr>
          </table>
        </div>

        <div class="detail-section" id="architecture">
          <h2>C. Technical Architecture</h2>
          <h4>Architecture Overview</h4><p>{esc(p['architecture']['overview'])}</p>
          <div class="mermaid">{mermaid_arch}</div>
          <h4>Components</h4><ul>{list_items(p['architecture']['components'])}</ul>
          <h4>Data Flow</h4><p>{esc(p['architecture']['dataflow'])}</p>
          <h4>Integration Architecture</h4><p>{esc(p['architecture']['integration'])}</p>
          {comparison_note}{when_to_use}
        </div>

        <div class="detail-section" id="stack">
          <h2>D. Technology Stack &amp; Rationale</h2>
          <table class="spec-table"><tr><th>Technology</th><th>Why It Was Selected</th></tr>{stack_rows}</table>
        </div>

        <div class="detail-section" id="hardware">
          <h2>E. Hardware Requirements</h2>
          <table class="spec-table">
            <tr><th>CPU</th><td>{esc(hw['cpu'])}</td></tr>
            <tr><th>GPU</th><td>{esc(hw['gpu'])}</td></tr>
            <tr><th>RAM</th><td>{esc(hw['ram'])}</td></tr>
            <tr><th>Storage</th><td>{esc(hw['storage'])}</td></tr>
            <tr><th>Networking</th><td>{esc(hw['networking'])}</td></tr>
            <tr><th>Recommended Configuration</th><td>{esc(hw['recommended'])}</td></tr>
          </table>
          <div class="note-box"><strong>Estimated, not tested:</strong> {esc(hw['note'])}</div>
        </div>

        <div class="detail-section" id="software">
          <h2>F. Software Architecture</h2>
          <table class="spec-table">
            <tr><th>Operating System</th><td>{esc(sw['os'])}</td></tr>
            <tr><th>Dependencies</th><td>{esc(', '.join(sw['dependencies']))}</td></tr>
            <tr><th>Services</th><td>{esc(', '.join(sw['services']) if isinstance(sw['services'], list) else esc(sw['services']))}</td></tr>
            <tr><th>Databases</th><td>{esc(', '.join(sw['databases']) if isinstance(sw['databases'], list) else esc(sw['databases']))}</td></tr>
            <tr><th>APIs</th><td>{esc(sw['apis'])}</td></tr>
            <tr><th>Monitoring</th><td>{esc(sw['monitoring'])}</td></tr>
            <tr><th>Automation</th><td>{esc(sw['automation'])}</td></tr>
          </table>
        </div>

        <div class="detail-section" id="roadmap">
          <h2>G. Implementation Roadmap</h2>
          <div class="mermaid">{mermaid_flow}</div>
          {roadmap_html}
        </div>

        <div class="detail-section" id="security">
          <h2>H. Security &amp; Reliability</h2>
          <table class="spec-table">
            <tr><th>Authentication</th><td>{esc(sec['authentication'])}</td></tr>
            <tr><th>Authorization</th><td>{esc(sec['authorization'])}</td></tr>
            <tr><th>Network Security</th><td>{esc(sec['network'])}</td></tr>
            <tr><th>Backup</th><td>{esc(sec['backup'])}</td></tr>
            <tr><th>Monitoring</th><td>{esc(sec['monitoring'])}</td></tr>
            <tr><th>Disaster Recovery</th><td>{esc(sec['dr'])}</td></tr>
            <tr><th>High Availability</th><td>{esc(sec['ha'])}</td></tr>
          </table>
        </div>

        <div class="detail-section" id="testing">
          <h2>I. Testing &amp; Validation</h2>
          <ul>{list_items(p['testing'])}</ul>
          <div class="note-box">Test scenarios describe planned validation criteria for this project's current status ({esc(p['status'])}). No completed test results are claimed here.</div>
        </div>

        <div class="detail-section" id="deliverables">
          <h2>J. Deliverables</h2>
          <ul>{list_items(p['deliverables'])}</ul>
        </div>

        <div class="detail-section" id="future">
          <h2>K. Future Enhancements</h2>
          <ul>{list_items(p['future'])}</ul>
        </div>

        <div class="detail-section" id="status">
          <h2>L. Project Status</h2>
          <span class="badge-status {p['statusClass']}" style="font-size:0.95rem;padding:10px 20px;"><span class="dot"></span>{esc(p['status'])}</span>
          <p class="text-muted" style="margin-top:14px;">This status reflects the current development stage honestly; it will be updated as work progresses.</p>
        </div>

        <div class="detail-section" id="cta" style="border-bottom:none;">
          <div class="cta-box">
            <h2 style="margin-bottom:14px;">Interested in developing similar infrastructure for your organization?</h2>
            <p class="lead" style="margin:0 auto 24px;">Let's discuss your technical requirements.</p>
            <a href="../contact.html" class="btn btn-primary">Contact / Collaborate</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.9.0/mermaid.min.js"></script>
<script>mermaid.initialize({{ startOnLoad: true, theme: 'dark' }});</script>
<style>@media (max-width:880px){{#projectLayout{{grid-template-columns:1fr !important;}} .toc-sticky{{position:static;}}}}</style>
"""
    out = page_shell(p["title"], p["short"], "projects", body, depth="../")
    write(f"projects/{p['slug']}.html", out)

# ---------------------------------------------------------------------------
# SEO FILES
# ---------------------------------------------------------------------------
def build_seo():
    urls = ["index.html", "about.html", "projects.html", "technologies.html", "architecture.html", "contact.html"]
    urls += [f"projects/{p['slug']}.html" for p in PROJECTS]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        sitemap += f"  <url><loc>{BASE_URL}/{u}</loc></url>\n"
    sitemap += "</urlset>\n"
    write("sitemap.xml", sitemap)
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n")

def write(relpath, content):
    full = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", relpath)

if __name__ == "__main__":
    build_home()
    build_about()
    build_projects_overview()
    build_technologies()
    build_architecture()
    build_contact()
    build_404()
    for p in PROJECTS:
        build_project_page(p)
    build_seo()
    print(f"\nBuild complete: {len(PROJECTS)} project pages + 7 site pages generated.")