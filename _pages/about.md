---
permalink: /
title: "欢迎访问王学荣的个人主页！"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
  /* 1. 基础折叠样式 */
  details > summary {
    list-style: none;
    cursor: pointer;
    padding: 5px 0;
    transition: color 0.2s;
    font-weight: normal; /* 默认字体不加粗，重点在内部加粗 */
  }
  
  /* 隐藏原生的小三角 */
  details > summary::-webkit-details-marker {
    display: none;
  }

  /* 2. 鼠标悬停时的反馈 */
  details > summary:hover {
    color: #0056b3; /* 悬停变色，提示可点击 */
    background-color: #f8f9fa; /* 轻微背景色，增强交互感 */
  }

  /* 3. 自定义旋转小三角 */
  .expand-icon {
    display: inline-block;
    color: #999;
    margin-right: 8px;
    font-size: 0.8em;
    transition: transform 0.2s ease;
  }
  .expand-icon::before {
    content: "►";
  }
  details[open] .expand-icon {
    transform: rotate(90deg);
  }

  /* 4. 引导点击的提示文字（右侧淡灰色小字） */
  .click-hint {
    float: right;
    font-size: 0.8em;
    color: #aaa;
    font-weight: normal;
    margin-right: 5px;
  }
  details[open] .click-hint {
    display: none; /* 展开后隐藏提示 */
  }

  /* 5. 展开后的详情框样式 */
  .details-content {
    margin-top: 5px; 
    margin-bottom: 15px;
    padding: 15px; 
    background-color: #f9f9f9; 
    border-left: 3px solid #0056b3; /* 左侧蓝线强调 */
    font-size: 0.95em;
    line-height: 1.6;
    text-align: justify; /* 确保内部内容也是两端对齐 */
  }

  /* 6. 详情框内的列表样式优化 */
  .details-content ul {
    margin: 0;
    padding-left: 20px;
  }
  .details-content li {
    margin-bottom: 5px;
  }
</style>

<div style="text-align: justify; text-justify: inter-word; hyphens: auto;" markdown="1">

我是王学荣（Duncan Wang），拥有超过30年的生物医药与化工行业经验，曾在多家跨国知名企业担任管理及技术职务。目前常驻中国上海，专注于行业技术咨询与管理工作。

<h1 style="border-bottom: 1px solid #e1e4e8; padding-bottom: 0.5em; margin-bottom: 0.3em; margin-top: 30px;">工作经历</h1>

* <details>
    <summary>
      <span class="expand-icon"></span>
      2021年02月 – 至今， <strong>独立灭菌技术专家</strong>， 邓肯灭菌工作室
      <span class="click-hint">(点击查看业绩)</span>
    </summary>
    <div class="details-content">
      主要负责环氧乙烷灭菌过程的开发、验证与确认，以及灭菌过程的改善与增效服务。
      <ul>
        <li><strong>技术开发与验证</strong>：负责新型环保+安全环氧乙烷灭菌过程的开发、验证和确认。</li>
        <li><strong>咨询与审核</strong>：提供灭菌过程专项审核、灭菌设备等同性证明、废气处理方案及安全数据咨询。</li>
        <li><strong>培训与指导</strong>：提供灭菌技术高级进阶培训，编写与审核灭菌过程控制文件及验证方案。</li>
      </ul>
    </div>
  </details>

* <details>
    <summary>
      <span class="expand-icon"></span>
      2021年01月 – 2021年02月， <strong>灭菌改进项目专家</strong>， 江苏省长丰医疗实业有限公司
      <span class="click-hint">(点击查看业绩)</span>
    </summary>
    <div class="details-content">
      <ul>
        <li>负责新型环保+安全环氧乙烷灭菌过程的开发、验证和确认。</li>
        <li>主导环氧乙烷灭菌过程废气处理专用设备的立项、设计与监理。</li>
      </ul>
    </div>
  </details>

* <details>
    <summary>
      <span class="expand-icon"></span>
      2017年07月 – 2020年12月， <strong>资深灭菌专家</strong>， 碧迪快速诊断产品（苏州）有限公司
      <span class="click-hint">(点击查看业绩)</span>
    </summary>
    <div class="details-content">
      <ul>
        <li><strong>工艺创新</strong>：建立了高效、低环氧乙烷残留的专用灭菌工艺；建立了灭菌装载升温曲线的数学模型，精准预测最冷点及升温时间。</li>
        <li><strong>验证与放行</strong>：验证了HYPAK产品的灭菌过程，并建立了基于灭菌参数放行的量化指标系统。</li>
        <li><strong>质量控制</strong>：建立了整套产品污染控制计划（包括洁净区监控、初始污染菌监控等），并组建了一支专业的无菌保证团队。</li>
      </ul>
    </div>
  </details>

* <details>
    <summary>
      <span class="expand-icon"></span>
      1997年11月 – 2016年09月， <strong>生产与质量管理经理</strong>， 金宝医疗器材上海（有限）公司
      <span class="click-hint">(点击查看业绩)</span>
    </summary>
    <div class="details-content">
      在职18年期间，全面负责质量体系建立、产品注册及生产工艺验证。
      <ul>
        <li><strong>体系建设</strong>：主导质量体系（ISO/GMP）及环境管理体系的建立与认证。</li>
        <li><strong>灭菌开发</strong>：负责环氧乙烷、蒸汽、辐照三种灭菌过程的开发与验证。</li>
        <li><strong>风险与合规</strong>：负责产品的风险分析、供应商审核、材料生物相容性评估及医疗器械产品的首次注册。</li>
      </ul>
    </div>
  </details>

* <details>
    <summary>
      <span class="expand-icon"></span>
      1993年03月 – 1997年11月， <strong>质量和法规经理</strong>， 上海莱士血液制品有限公司
      <span class="click-hint">(点击查看业绩)</span>
    </summary>
    <div class="details-content">
      <ul>
        <li><strong>GMP认证</strong>：按照cGMP要求建立了血液制品生产的质量管理体系，并成功通过SFDA认证。</li>
        <li><strong>技术攻关</strong>：对人血丙种球蛋白、第八因子等4个关键产品的工艺研发与确认做出关键贡献；建立了病毒灭活可靠性验证体系。</li>
        <li><strong>风险控制</strong>：建立了全流程风险管理体系，实现产品关键质量项目零投诉。</li>
      </ul>
    </div>
  </details>

* <details>
    <summary>
      <span class="expand-icon"></span>
      1991年09月 – 1993年02月， <strong>研发部主管</strong>， 杜邦农化（上海）有限公司
      <span class="click-hint">(点击查看业绩)</span>
    </summary>
    <div class="details-content">
      <ul>
        <li>与美国杜邦总部（Experiment Station）技术合作，全面引进Londax过程控制技术。</li>
        <li>建立了农得时（Londax）产品的质量分析与控制方法，并负责其复合制剂的本地化开发。</li>
      </ul>
    </div>
  </details>

* 1990年09月 – 1991年09月， <strong>助理研究员</strong>， 中国科学院上海昆虫研究所

<h1 style="border-bottom: 1px solid #e1e4e8; padding-bottom: 0.5em; margin-bottom: 0.3em; margin-top: 30px;">教育背景</h1>

* 1985年09月 – 1990年09月， **中国科学院上海药物研究所**， 有机化学专业， 博士学位
* 1980年09月 – 1985年07月， **华东师范大学**， 化学专业（高分子材料方向）， 学士学位

</div>
