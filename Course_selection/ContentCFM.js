// Function to create HTML content from JSON data
function generateHTML(data) {
    const contentDiv = document.getElementById("layout1");
  
    // Loop through each section
    data.forEach(section => {
      const sectionElement = document.createElement("section");
      sectionElement.id = section.SectionTag;
  
      // Create and append the Section Title
      const h1 = document.createElement("h1");
      h1.textContent = section.SectionContentBrief.join(', ');
      sectionElement.appendChild(h1);
  
      // Create and append the "Contents" header
      const h2 = document.createElement("h2");
      h2.textContent = "Contents:";
      sectionElement.appendChild(h2);
  
      // Create and append the unordered list for the brief content
      const ul = document.createElement("ul");
      section.SectionContentBrief.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item;
        ul.appendChild(li);
      });
      sectionElement.appendChild(ul);
  
      // Embed the video
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
  
      // Add horizontal rule to separate sections
      sectionElement.appendChild(document.createElement("hr"));
  
      // Loop through each course and create its content
      section.courses.forEach(course => {
        const courseH1 = document.createElement("h1");
        courseH1.textContent = course.course_name;
        sectionElement.appendChild(courseH1);
  
        // Create div for grade levels
        const div = document.createElement("div");
        course.grade_levels.forEach(grade => {
          const span = document.createElement("span");
          span.classList.add(`grade${grade}`);
          span.textContent = grade;
          div.appendChild(span);
        });
  
        // Append elective label
        const elecSpan = document.createElement("span");
        elecSpan.classList.add("elec");
        elecSpan.textContent = "Elective";
        div.appendChild(elecSpan);
        sectionElement.appendChild(div);
  
        // Create and append course codes
        course.course_codes.forEach(code => {
          const courseCodeH2 = document.createElement("h2");
          courseCodeH2.textContent = `Course Code: ${code}`;
          sectionElement.appendChild(courseCodeH2);
        });
  
        // Append the course description
        const descriptionP = document.createElement("p");
        descriptionP.classList.add("texts");
        descriptionP.innerHTML = course.description;
        sectionElement.appendChild(descriptionP);
  
        // Append prerequisite if any
        if (course.prerequisite) {
          const prerequisiteP = document.createElement("p");
          prerequisiteP.classList.add("texts");
          prerequisiteP.innerHTML = `<b>(${course.prerequisite})</b><br>`;
          sectionElement.appendChild(prerequisiteP);
        }
  
        // Add a horizontal rule after each course
        sectionElement.appendChild(document.createElement("hr"));
      });
  
      // Append the section element to the content div
      contentDiv.appendChild(sectionElement);
    });
  }
  
  // Fetch the JSON data from the file
  fetch('Tech_Ed_Info.json')
    .then(response => response.json())
    .then(data => {
      // Generate the HTML content from the fetched JSON data
      generateHTML(data);
    })
    .catch(error => {
      console.error('Error loading the JSON file:', error);
    });
  