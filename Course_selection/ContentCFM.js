// Function to create HTML content from JSON data
function generateHTML(data) {
    const contentDiv = document.getElementById("content");
  
    // Loop through each section
    data.forEach(section => {
      const sectionElement = document.createElement("section");
      sectionElement.id = section.SectionTag;
  
      const h1 = document.createElement("h1");
      h1.textContent = section.SectionContentBrief.join(', ');
      sectionElement.appendChild(h1);
  
      const h2 = document.createElement("h2");
      h2.textContent = "Contents:";
      sectionElement.appendChild(h2);
  
      const ul = document.createElement("ul");
      ul.id = "lit";
      section.SectionContentBrief.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item;
        ul.appendChild(li);
      });
      sectionElement.appendChild(ul);
  
      const center = document.createElement("center");
      const iframe = document.createElement("iframe");
      iframe.width = "560";
      iframe.height = "315";
      iframe.src = section.VideoLink;
      iframe.title = "YouTube video player";
      iframe.frameborder = "0";
      iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
      iframe.allowfullscreen = true;
      center.appendChild(iframe);
      sectionElement.appendChild(center);
  
      sectionElement.appendChild(document.createElement("hr"));
      sectionElement.appendChild(document.createElement("hr"));
  
      // Loop through each course and create its content
      section.courses.forEach(course => {
        const courseH1 = document.createElement("h1");
        courseH1.textContent = course.course_name;
        sectionElement.appendChild(courseH1);
  
        const div = document.createElement("div");
        course.grade_levels.forEach(grade => {
          const span = document.createElement("span");
          span.classList.add(`grade${grade}`);
          span.textContent = grade;
          div.appendChild(span);
        });
        const elecSpan = document.createElement("span");
        elecSpan.classList.add("elec");
        elecSpan.textContent = "Elective";
        div.appendChild(elecSpan);
        sectionElement.appendChild(div);
  
        course.course_codes.forEach(code => {
          const courseCodeH2 = document.createElement("h2");
          courseCodeH2.textContent = `Course Code: ${code}`;
          sectionElement.appendChild(courseCodeH2);
        });
  
        const descriptionP = document.createElement("p");
        descriptionP.classList.add("texts");
        descriptionP.innerHTML = course.description;
        sectionElement.appendChild(descriptionP);
  
        if (course.prerequisite) {
          const prerequisiteP = document.createElement("p");
          prerequisiteP.classList.add("texts");
          prerequisiteP.innerHTML = `<b>(${course.prerequisite})</b><br>`;
          sectionElement.appendChild(prerequisiteP);
        }
  
        sectionElement.appendChild(document.createElement("hr"));
      });
  
      contentDiv.appendChild(sectionElement);
    });
  }
  
  // Fetch the JSON data from the file
  fetch('data.json')
    .then(response => response.json())
    .then(data => {
      // Generate the HTML content from the fetched JSON data
      generateHTML(data);
    })
    .catch(error => {
      console.error('Error loading the JSON file:', error);
    });
  