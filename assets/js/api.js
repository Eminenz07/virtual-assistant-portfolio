/**
 * Portfolio CMS API Integration
 * Fetches content from Django backend and renders it dynamically.
 */

const API_BASE_URL = 'https://excellenceeniola.fly.dev/api';
// const API_BASE_URL = 'https://your-production-url.com/api'; // Change for production

document.addEventListener("DOMContentLoaded", () => {
  fetchServices();
  fetchTestimonials();
  fetchExperience();
  fetchSkills();
  fetchCertifications();
  fetchProjects();
  fetchBlogs();
});

// --- Helper to fetch data ---
async function fetchData(endpoint) {
  try {
    const response = await fetch(`${API_BASE_URL}/${endpoint}/`);
    if (!response.ok) throw new Error(`Error fetching ${endpoint}`);
    return await response.json();
  } catch (error) {
    console.error(error);
    return [];
  }
}

// --- Helper to normalize paths ---
function normalizePath(path) {
    if (!path) return '';
    // Fix seed data paths
    if (path.startsWith('./assets/')) {
        return path.replace('./assets/', '/static/');
    }
    // Fix other relative paths if needed
    if (path.startsWith('assets/')) {
        return '/static/' + path.substring(7);
    }
    return path;
}

// --- 1. What I Do ---
async function fetchServices() {
  const data = await fetchData("whatido");
  const container = document.querySelector(".service-list");
  if (!container || data.length === 0) return;

  container.innerHTML = data
    .map(
      (item) => `
        <li class="service-item">
            <div class="service-icon-box">
                <ion-icon name="${item.icon_name || 'create-outline'}"></ion-icon>
            </div>
            <div class="service-content-box">
                <h4 class="h4 service-item-title">${item.title}</h4>
                <p class="service-item-text">${item.description}</p>
            </div>
        </li>
    `
    )
    .join("");
}

// --- 2. Testimonials ---
async function fetchTestimonials() {
  const data = await fetchData("testimonials");
  const container = document.querySelector(".testimonials-list");
  if (!container || data.length === 0) return;

  container.innerHTML = data
    .map(
      (item) => `
        <li class="testimonials-item">
            <div class="content-card" data-testimonials-item>
                <figure class="testimonials-avatar-box">
                    <img src="${
                      normalizePath(item.client_image) || "/static/images/avatar-1.png"
                    }" alt="${
        item.client_name
      }" width="60" data-testimonials-avatar>
                </figure>
                <h4 class="h4 testimonials-item-title" data-testimonials-title>${
                  item.client_name
                }</h4>
                <h5 class="h5 testimonials-item-sub-title" data-testimonials-title>${
                  item.designation
                }</h5>
                <div class="testimonials-text" data-testimonials-text>
                    <p>${item.testimonial_text}</p>
                </div>
            </div>
        </li>
    `
    )
    .join("");
}
// ... (skipping non-image sections for brevity, but they should be preserved if I used replace_file_content correctly)
// Wait, I cannot skip with replace_file_content unless I target specific blocks.
// I will target specific blocks to replace.

// --- 5. Certifications ---
async function fetchCertifications() {
  const data = await fetchData("certifications");
  const container = document.querySelector(".certifications-list");
  if (!container || data.length === 0) return;

  container.innerHTML = data
    .map(
      (item) => `
        <li class="certification-item">
            <a href="${item.credential_url || "#"}" target="_blank">
                <figure class="certification-banner-box">
                    <img src="${
                      normalizePath(item.certificate_image) || "/static/images/cert1.jpg"
                    }" alt="${item.title}" loading="lazy">
                </figure>
                <div class="certification-content">
                    <h3 class="h3 certification-item-title">${item.title}</h3>
                    <p class="certification-text">${item.issuer} - ${
        item.date_earned
      }</p>
                </div>
            </a>
        </li>
    `
    )
    .join("");
}

// --- 6. Projects ---
async function fetchProjects() {
  const data = await fetchData("projects");
  const container = document.querySelector(".project-list");
  if (!container || data.length === 0) return;

  container.innerHTML = data
    .map(
      (item) => `
        <li class="project-item active" data-filter-item data-category="all">
            <a href="${
              item.link_live || item.link_repo || "#"
            }" target="_blank">
                <figure class="project-img">
                    <div class="project-item-icon-box">
                        <ion-icon name="eye-outline"></ion-icon>
                    </div>
                    <img src="${normalizePath(item.cover_image)}" alt="${
        item.title
      }" loading="lazy">
                </figure>
                <h3 class="project-title">${item.title}</h3>
                <p class="project-category">${item.description}</p>
            </a>
        </li>
    `
    )
    .join("");
}

// --- 7. Blogs ---
async function fetchBlogs() {
  const data = await fetchData("blogs");
  const blogArticle = document.querySelector('article[data-page="blog"]');
  if (!blogArticle) return; 

  let container = blogArticle.querySelector(".research-posts-list");
  if (!container) {
    const header = blogArticle.querySelector("header");
    container = document.createElement("ul");
    container.className = "research-posts-list";
    if (header) header.after(container);
    else blogArticle.appendChild(container);
  }

  if (data.length === 0) {
    container.innerHTML = "<p>No blog posts found.</p>";
    return;
  }

  container.innerHTML = data
    .map(
      (item) => `
        <li class="research-post-item">
            <a href="#">
                <figure class="research-banner-box">
                    <img src="${normalizePath(item.cover_image)}" alt="${
        item.title
      }" loading="lazy">
                </figure>
                <div class="research-content">
                    <div class="research-meta">
                        <p class="research-category">${item.tags}</p>
                        <span class="dot"></span>
                        <time datetime="${item.published_date}">${
        item.published_date
      }</time>
                    </div>
                    <h3 class="h3 research-item-title">${item.title}</h3>
                    <p class="research-text">${typeof marked !== 'undefined' ? marked.parse(item.markdown_body).substring(0, 100) : item.markdown_body.substring(0, 100)}...</p>
                </div>
            </a>
        </li>
    `
    )
    .join("");
}

// --- 3. Experience ---
async function fetchExperience() {
  const data = await fetchData("experience");
  // Target the experience timeline specifically.
  // Assuming the structure: Education Timeline -> Experience Timeline
  // We look for the h3 "Experience" and then the following list.
  const experienceHeader = Array.from(
    document.querySelectorAll(".timeline .h3")
  ).find((el) => el.textContent.includes("Experience"));
  if (!experienceHeader) return;

  const container = experienceHeader
    .closest(".timeline")
    .querySelector(".timeline-list");
  if (!container || data.length === 0) return;

  container.innerHTML = data
    .map(
      (item) => `
        <li class="timeline-item">
            <h4 class="h4 timeline-item-title">${item.role}</h4>
            <h5 class="h5 timeline-item-title">${item.company}</h5>
            <span>${item.start_date} – ${
        item.is_current ? "Present" : item.end_date
      }</span>
            <p class="timeline-text">${item.description}</p>
        </li>
    `
    )
    .join("");
}

// --- 4. Skills ---
async function fetchSkills() {
  const data = await fetchData("skills");
  // Assumption: Two columns of skills in index.html, we might just merge them or split them
  // For simplicity, we'll try to populate the existing lists or create a new single list
  // The template has two ".skills-list" in ".column". We'll clear both and just fill the first one or distribute.

  // Simple strategy: Clear all cols, append to first or create a combined list.
  const allLists = document.querySelectorAll(".skills-list");
  if (allLists.length === 0 || data.length === 0) return;

  // Clear everything first
  allLists.forEach((list) => (list.innerHTML = ""));

  // Distribute evenly
  const half = Math.ceil(data.length / 2);
  const col1 = data.slice(0, half);
  const col2 = data.slice(half);

  function renderSkillItem(skill) {
    return `
        <li class="skills-item">
            <div class="title-wrapper">
                <h5 class="h5">${skill.name}</h5>
                <data value="${skill.proficiency}">${skill.proficiency}%</data>
            </div>
            <div class="skill-progress-bg">
                <div class="skill-progress-fill" style="width: ${skill.proficiency}%;"></div>
            </div>
        </li>`;
  }

  if (allLists[0]) allLists[0].innerHTML = col1.map(renderSkillItem).join("");
  if (allLists[1]) allLists[1].innerHTML = col2.map(renderSkillItem).join("");
}

// --- 5. Certifications ---
async function fetchCertifications() {
  const data = await fetchData("certifications");
  const container = document.querySelector(".certifications-list");
  if (!container || data.length === 0) return;

  container.innerHTML = data
    .map(
      (item) => `
        <li class="certification-item">
            <a href="${item.credential_url || "#"}" target="_blank">
                <figure class="certification-banner-box">
                    <img src="${
                      item.certificate_image || "./assets/images/cert1.jpg"
                    }" alt="${item.title}" loading="lazy">
                </figure>
                <div class="certification-content">
                    <h3 class="h3 certification-item-title">${item.title}</h3>
                    <p class="certification-text">${item.issuer} - ${
        item.date_earned
      }</p>
                </div>
            </a>
        </li>
    `
    )
    .join("");
}

// --- 6. Projects ---
async function fetchProjects() {
  const data = await fetchData("projects");
  const container = document.querySelector(".project-list");
  if (!container || data.length === 0) return;

  // Filter logic is present in HTML (All, Web design, etc). We might just show everything for 'All'.
  // The current HTML has filtered items. We'll just append simple items.

  container.innerHTML = data
    .map(
      (item) => `
        <li class="project-item active" data-filter-item data-category="all">
            <a href="${
              item.link_live || item.link_repo || "#"
            }" target="_blank">
                <figure class="project-img">
                    <div class="project-item-icon-box">
                        <ion-icon name="eye-outline"></ion-icon>
                    </div>
                    <img src="${item.cover_image}" alt="${
        item.title
      }" loading="lazy">
                </figure>
                <h3 class="project-title">${item.title}</h3>
                <p class="project-category">${item.description}</p>
            </a>
        </li>
    `
    )
    .join("");
}

// --- 7. Blogs ---
async function fetchBlogs() {
  const data = await fetchData("blogs");
  // Assuming there is a blog list container. If not, we might need to add it or target a placeholder.
  // Based on 'index.html', there is a 'Blog' nav but I haven't seen the section.
  // I'll assume a section with class 'blog-posts-list' exists or I target the 'article.blog'

  // If the article exists but list doesn't, we create it
  const blogArticle = document.querySelector('article[data-page="blog"]');
  if (!blogArticle) return; // Exit if page not found

  let container = blogArticle.querySelector(".blog-posts-list");
  if (!container) {
    // Create the list if it doesn't exist
    const header = blogArticle.querySelector("header");
    container = document.createElement("ul");
    container.className = "blog-posts-list";
    if (header) header.after(container);
    else blogArticle.appendChild(container);
  }

  if (data.length === 0) {
    container.innerHTML = "<p>No blog posts found.</p>";
    return;
  }

  container.innerHTML = data
    .map(
      (item) => `
        <li class="blog-post-item">
            <a href="#">
                <figure class="blog-banner-box">
                    <img src="${item.cover_image}" alt="${
        item.title
      }" loading="lazy">
                </figure>
                <div class="blog-content">
                    <div class="blog-meta">
                        <p class="blog-category">${item.tags}</p>
                        <span class="dot"></span>
                        <time datetime="${item.published_date}">${
        item.published_date
      }</time>
                    </div>
                    <h3 class="h3 blog-item-title">${item.title}</h3>
                    <p class="blog-text">${typeof marked !== 'undefined' ? marked.parse(item.markdown_body).substring(0, 100) : item.markdown_body.substring(0, 100)}...</p>
                </div>
            </a>
        </li>
    `
    )
    .join("");
}
