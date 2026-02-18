---
permalink: /english/
title: "Welcome to Dr. Wang's Personal Homepage!"
author_profile: true
---

<style>
  /* ====================
     1. Product Showcase Styles (Resized)
     ==================== */
  .product-item {
    display: flex; /* Flex layout for left-image right-text */
    align-items: center; /* Vertically align center */
    margin-bottom: 20px; /* Spacing between items */
    padding: 15px; /* Padding */
    border: 1px solid #f0f0f0; 
    border-radius: 6px; 
    background-color: #fff;
    transition: box-shadow 0.2s;
  }
  
  .product-item:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.08); /* Darker shadow on hover */
  }

  /* Left Image Container - Width increased from 120px to 170px (+40%) */
  .product-img-box {
    flex: 0 0 170px; 
    margin-right: 25px; /* Increased spacing */
    border-radius: 4px;
    overflow: hidden;
    border: 1px solid #eee;
    background-color: #f9f9f9;
  }

  /* Image styling */
  .product-img-box img {
    display: block;
    width: 100%;
    height: auto;
    aspect-ratio: 4 / 3; /* Lock 4:3 aspect ratio */
    object-fit: cover; 
    margin: 0; 
  }

  /* Right Text Container */
  .product-info {
    flex: 1; 
    font-size: 0.95em;
    line-height: 1.6;
  }

  .product-name {
    font-weight: bold;
    font-size: 1.2em; /* Slightly larger title */
    color: #333;
    display: block;
    margin-bottom: 6px;
  }

  .product-spec {
    color: #666;
    font-size: 0.95em;
    display: block; /* Takes up its own line */
    margin-bottom: 6px;
  }

  .product-desc {
    color: #444;
    font-size: 0.95em;
    display: block;
    /* Placeholder for specific description styles */
  }

  /* ====================
     2. Interaction and Fold Styles (Unchanged)
     ==================== */
  details > summary {
    list-style: none;
    cursor: pointer;
    padding: 0; 
    transition: color 0.2s;
  }
  
  details > summary::-webkit-details-marker { display: none; }

  details > summary:hover { color: #0056b3; }

  .expand-icon {
    color: #999;
    margin-left: 5px; 
    margin-right: 0px;
    font-size: 0.8em;
    display: inline-block;
    transition: transform 0.2s ease;
  }
  
  details > summary:hover .expand-icon { color: #333; }

  .expand-icon::before { content: "►"; }
  
  details[open] .expand-icon { transform: rotate(90deg); }

  .details-content {
    margin-top: 5px; 
    margin-bottom: 10px; 
    padding: 15px; 
    background-color: #f9f9f9; 
    border-left: 3px solid #ccc; 
    font-size: 0.95em;
    line-height: 1.6;
    text-align: justify; 
  }

  .section-sub-title {
    font-weight: bold;
    color: #333;
    margin-top: 10px;
    margin-bottom: 5px;
    display: block;
  }
  .section-sub-title:first-child { margin-top: 0; }

  .details-content ul { margin: 0; padding-left: 20px; }
  .details-content li { margin-bottom: 3px; }
</style>

<div style="text-align: justify; text-justify: inter-word; hyphens: auto;" markdown="1">

I am Dr. Xuerong (Duncan) Wang, possessing over 30 years of experience in quality and regulatory management as well as product R&D management within multinational corporations in the medical device and pharmaceutical industries. I possess comprehensive technical knowledge and experience across the full spectrum of Ethylene Oxide (EO) sterilization, irradiation sterilization, and moist heat steam sterilization.

<h1 style="border-bottom: 1px solid #e1e4e8; padding-bottom: 0.5em; margin-bottom: 0.3em; margin-top: 30px;">Featured Products</h1>

<div class="product-item">
  <div class="product-img-box">
    <img src="https://via.placeholder.com/600x450/e0e0e0/888888?text=Product+1" alt="EO Standard">
  </div>
  <div class="product-info">
    <span class="product-name">Ethylene Oxide Working Standard (EO)</span>
    <span class="product-spec">Spec: 10 mg/mL</span>
    <span class="product-desc">Product Description:</span> 
  </div>
</div>

<div class="product-item">
  <div class="product-img-box">
    <img src="https://via.placeholder.com/600x450/e0e0e0/888888?text=Product+2" alt="ECH Standard">
  </div>
  <div class="product-info">
    <span class="product-name">2-Chloroethanol Working Standard (ECH)</span>
    <span class="product-spec">Spec: 50 mg/mL</span>
    <span class="product-desc">Product Description:</span>
  </div>
</div>

<div class="product-item">
  <div class="product-img-box">
    <img src="https://via.placeholder.com/600x450/e0e0e0/888888?text=Product+3" alt="Chemical Indicator Probe">
  </div>
  <div class="product-info">
    <span class="product-name">Chemical Indicator Probe</span>
    <span class="product-spec">Size: 2 mm * 10 mm</span>
    <span class="product-desc">Product Description:</span>
  </div>
</div>


<h1 style="border-bottom: 1px solid #e1e4e8; padding-bottom: 0.5em; margin-bottom: 0.3em; margin-top: 30px;">Professional Experience</h1>

* <details>
    <summary>
      Feb 2021 – Present<span class="expand-icon"></span>, <strong>Independent Sterilization Technical Expert</strong>, Duncan Sterilization Studio
    </summary>
    <div class="details-content">
      <span class="section-sub-title">Job Description:</span>
      <ul>
        <li>Development, validation, and confirmation of novel eco-friendly and safe Ethylene Oxide (EO) sterilization processes.</li>
        <li>Improvement and efficiency enhancement services for existing EO sterilization processes.</li>
        <li>Specialized audit services for EO sterilization processes.</li>
        <li>Design and customization services for Process Challenge Devices (PCD) for EO sterilization.</li>
        <li>Design services for packaging and sterilization load configurations for EO sterilized products.</li>
        <li>Consultation and services for proving sterilization equipment equivalence.</li>
        <li>Consultation and services regarding safety data, physicochemical properties, and flammability/explosion characteristics of EO sterilization gas.</li>
        <li>Consultation and services for waste gas treatment in EO sterilization processes.</li>
        <li>Design, manufacturing supervision, and installation services for dedicated waste gas treatment equipment for EO sterilization.</li>
        <li>Consultation and services for EO sterilization, irradiation sterilization, and moist heat steam sterilization.</li>
        <li>Consultation and services for EO concentration monitoring.</li>
        <li>Consultation and services for calibration of EO concentration probes.</li>
        <li>Routine periodic parameter audit services for sterilization processes.</li>
        <li>Second-party audit agency services for sterilization service providers, including tracking and resolution of non-conformities.</li>
        <li>Pre-audit services prior to important external audits for EO, irradiation, and moist heat steam sterilization.</li>
        <li>Investigation and resolution services for process deviations and complex issues in EO, irradiation, and moist heat steam sterilization.</li>
        <li>Consultation and services for microbiological control in sterile product manufacturing.</li>
        <li>Validation of product bioburden, Bacteriostasis & Fungistasis (B&F) suitability testing, and product sterility testing related to sterilization.</li>
        <li>Specialized audit services for microbiological control and testing in sterile product manufacturing.</li>
        <li>Drafting and review services for sterilization process control documents.</li>
        <li>Drafting and review services for sterilization process validation protocols and reports.</li>
        <li>Review services for protocols and reports regarding product bioburden, B&F suitability testing, and product sterility testing.</li>
        <li>Consultation and services for safety, environmental protection, and occupational health in EO sterilization processes.</li>
        <li>Advanced training services in sterilization technology.</li>
        <li>Preparation and review services for sterilization-related content in product registration dossiers.</li>
      </ul>
    </div>
  </details>

* <details>
    <summary>
      Jan 2021 – Feb 2021<span class="expand-icon"></span>, <strong>Sterilization Improvement Project Expert</strong>, Jiangsu Changfeng Medical Industry Co., Ltd.
    </summary>
    <div class="details-content">
      <span class="section-sub-title">Job Description:</span>
      <ul>
        <li>Development, validation, and confirmation of novel eco-friendly and safe EO sterilization processes.</li>
        <li>Project initiation, design, and supervision of dedicated waste gas treatment equipment for EO sterilization processes.</li>
      </ul>
    </div>
  </details>

* <details>
    <summary>
      Jul 2017 – Dec 2020<span class="expand-icon"></span>, <strong>Senior Sterilization Lead</strong>, BD Rapid Diagnostic products (Suzhou) Co., Ltd.
    </summary>
    <div class="details-content">
      <span class="section-sub-title">Job Description:</span>
      <ul>
        <li>Responsible for sterility assurance of Hypak products to achieve comprehensive performance goals in quality, regulations, cost, and efficiency.</li>
        <li>Established operating procedures for sterilization and production environment control and monitoring; supervised strict execution of procedures; conducted periodic assessments to improve the effectiveness of sterilization and sterility assurance.</li>
        <li>Formulated sterilization validation plans; drafted and executed validation protocols according to the plan, including validation and re-validation of sterilization processes.</li>
        <li>Compiled standardized batch records for sterilized products to ensure all production control elements were accurately and appropriately recorded, meeting product traceability requirements.</li>
        <li>Managed validation execution of sterilization and microbiology service suppliers; managed quality assurance activities related to sterilization suppliers and outsourcing suppliers, including technical agreements, audits, deviation investigation and handling, complaints, and BD customer visits.</li>
        <li>Provided advanced professional training on sterilization technology to team colleagues.</li>
        <li>Regularly communicated with BD Asia Pacific and BD Global Sterilization Teams to ensure consistency and coordination in sterilization and microbiology-related control matters, while ensuring compliance with domestic laws and regulations.</li>
        <li>Regularly aggregated and analyzed data related to sterilization and contamination control; participated in management reviews.</li>
        <li>Managed CAPA activities related to sterilization.</li>
      </ul>
      <span class="section-sub-title">Key Achievements:</span>
      <ul>
        <li>Established a high-efficiency EO sterilization process with low EO residuals.</li>
        <li>Validated the EO sterilization process for HYPAK products and established a quantitative indicator system for parametric release based on sterilization parameters.</li>
        <li>Established a mathematical model for the sterilization load heating curve to predict the "cold spot" of the load and calculate the time to reach minimum sterilization temperature.</li>
        <li>Established a complete product contamination control plan and implementation scheme (including personnel entry/exit requirements for clean areas, environmental contamination monitoring points, initial bioburden monitoring, and various detection methods in the microbiology laboratory).</li>
        <li>Built and trained a capable sterility assurance team for sterilization and microbiological contamination control.</li>
      </ul>
    </div>
  </details>

* <details>
    <summary>
      Nov 1997 – Oct 2016<span class="expand-icon"></span>, <strong>QRM</strong>, Gambro Medical products  (Shanghai) Co.,Ltd.
    </summary>
    <div class="details-content">
      <span class="section-sub-title">Job Description:</span>
      <ul>
        <li>Responsible for quality system management and continuous improvement.</li>
        <li>Responsible for customer complaint management and continuous improvement of customer satisfaction.</li>
        <li>Responsible for coordinating CAPA projects and continuously improving quality costs.</li>
        <li>Set departmental goals, monitored departmental performance, identified departmental training needs, and supervised team members.</li>
        <li>Managed inspections and laboratory testing (chemical, biological, physical).</li>
        <li>Managed product validation and process validation.</li>
        <li>Responsible for localization of products and processes.</li>
        <li>Managed sterilization validation and routine monitoring of products (including EO sterilization, steam sterilization, and E-beam sterilization).</li>
        <li>Production Quality Management: Routine production quality management, production and product release.</li>
        <li>Responsible for providing technical standards and documents for material procurement to the purchasing department.</li>
        <li>Routine Quality Reporting: Established annual quality KPI indicators and reviewed monthly KPI reports.</li>
        <li>Team Management: Performance goal setting and assessment; recruitment and interviewing; financial budgeting and control, etc.</li>
        <li>Responsible for medical device product registration.</li>
        <li>Responsible for providing relevant standard quality documentation packages for the marketing department (sales companies, distributors) to participate in domestic and international market tenders.</li>
        <li>Responsible for assessing suppliers of critical materials and sterilization processes.</li>
      </ul>
      <span class="section-sub-title">Key Achievements:</span>
      <ul>
        <li>Participated in the startup team to relocate the production line from Gambro's Chiga factory in Japan to Shanghai; established the Shanghai quality team and facilities.</li>
        <li>Established the ISO 13485 quality system and obtained certification.</li>
        <li>Obtained CE product registration certification in 1999, allowing products to independently enter the European market.</li>
        <li>Established the ISO 14001 environmental management system and obtained certification.</li>
        <li>Established and promoted Kaizen/CAPA/PDCA to continuously improve quality costs.</li>
        <li>Obtained the first product registration certificate for blood tubing (Class III) products in China in 1998.</li>
        <li>Completed the localization task for PVC materials and sterilization process localization, reducing product costs by 40%.</li>
        <li>Completed the localization task for radiation-resistant PVC materials, clearing obstacles for the introduction of E-beam sterilization methods.</li>
        <li>Improved EO sterilization parameters, increasing sterilization efficiency by 15% and saving sterilization costs.</li>
        <li>Established validation template documents for critical processes such as injection molding, extrusion, sterilization, and sterile packaging.</li>
        <li>Established assessment document templates for all blood-contact materials in accordance with ISO 10993.1.</li>
        <li>Established monitoring methods for the sensitivity and accuracy of leakage tester systems.</li>
        <li>Established assessment methods for the sterile shelf life of product sterile packaging.</li>
        <li>Responsible for assessing products from critical suppliers (infusion sets, sterile air sensors, waste liquid collection bags, plastic puncture needles, sterile packaging materials) and critical processes (four EO sterilization suppliers, three E-beam sterilization suppliers, etc.). Audit standards included ISO 13485 (QMS), 21 CFR 820 (cGMP), ISO 11135 (EO Sterilization), and ISO 11607 (Packaging for Terminally Sterilized Medical Devices), covering both quality systems and critical production/testing processes.</li>
        <li>Responsible for risk assessment and control of product design changes, cooperating with the purchasing department on cost-saving projects.</li>
        <li>Compiled CE Technical Files: Completed updates to relevant technical file compilations and various technical tasks.</li>
      </ul>
    </div>
  </details>

* <details>
    <summary>
      Feb 1993 – Nov 1997<span class="expand-icon"></span>, <strong>QRM</strong>, Shanghai RAAS Blood products Co., Ltd.
    </summary>
    <div class="details-content">
      <span class="section-sub-title">Job Responsibilities:</span>
      <ul>
        <li>Responsible for new product development.</li>
        <li>Responsible for establishing standards for raw materials, intermediates, and finished products.</li>
        <li>Establishment, certification, and continuous improvement of the quality management system.</li>
        <li>Responsible for supervising the implementation of product process documents.</li>
        <li>Responsible for risk management and control activities for blood products, and reliability validation of viral inactivation processes.</li>
        <li>Responsible for the compilation and consolidation of new product registration documents for blood products.</li>
        <li>Responsible for post-market surveillance of blood products.</li>
        <li>Quality Assurance Team Building: Personnel planning, recruitment, training, assessment, etc.</li>
        <li>Responsible for product registration and communication with the SFDA (State Food and Drug Administration).</li>
      </ul>
      <span class="section-sub-title">Key Achievements:</span>
      <ul>
        <li>Established a quality management system for blood product production in accordance with cGMP requirements and obtained SFDA certification.</li>
        <li>Established a risk management control system for blood products. Implemented risk management in all aspects of production and product design changes, achieving zero complaints for critical product quality items.</li>
        <li>Made critical contributions to the process R&D and process confirmation of 4 blood products (Human Albumin, Prothrombin Complex, Factor VIII, Fibrinogen).</li>
        <li>Established a reliability validation system for viral inactivation.</li>
        <li>Established an assessment system for raw material manufacturers.</li>
      </ul>
    </div>
  </details>

* <details>
    <summary>
      Sep 1991 – Feb 1993<span class="expand-icon"></span>, <strong>R&D Supervisor</strong>, Shanghai DuPont Agriculture products Co., Ltd.
    </summary>
    <div class="details-content">
      <span class="section-sub-title">Job Description:</span>
      <ul>
        <li>Participated in the Londax project, collaborating with technical personnel from DuPont's Experiment Station in the USA to comprehensively introduce Londax process control technology.</li>
        <li>Established quality analysis and control methods for 10% Londax wettable powder.</li>
        <li>Responsible for the localization development of Londax compound formulations.</li>
      </ul>
    </div>
  </details>

* <details>
    <summary>
      Sep 1990 – Sep 1991<span class="expand-icon"></span>, <strong>Lab chief</strong>, Shanghai Institute of Entomology, Chinese Academy of Sciences
    </summary>
    <div class="details-content">
      <span class="section-sub-title">Job Description:</span>
      <ul>
        <li>Responsible for the synthesis and application research of insect pheromones.</li>
        <li>Responsible for the management of the chemistry laboratory.</li>
        <li>Developed and designed novel insect traps.</li>
      </ul>
      <span class="section-sub-title">Key Achievements:</span>
      <ul>
        <li>Synthesized the pheromone of the poplar clearwing moth (Paranthrene tabaniformis) and successfully trapped the target pest in vineyards.</li>
      </ul>
    </div>
  </details>

<h1 style="border-bottom: 1px solid #e1e4e8; padding-bottom: 0.5em; margin-bottom: 0.3em; margin-top: 30px;">Education</h1>

* Sep 1985 – Sep 1990, **Shanghai Institute of Materia Medica, Chinese Academy of Sciences**, Ph.D. in Organic Chemistry
* Sep 1980 – Jul 1985, **East China Normal University**, B.S. in Chemistry (Polymer Science)

</div>
