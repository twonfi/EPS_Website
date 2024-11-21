document.addEventListener("DOMContentLoaded", () => {
    const contentContainer = document.getElementById("layout1");
  
    // Fetch the content from the JSON file
    fetch("content.json")
      .then((response) => response.json())
      .then((data) => {
        const courses = data.courses;
  
        // Dynamically populate courses
        courses.forEach((course) => {
          const courseDiv = document.createElement("div");
  
          // Course Title
          const title = document.createElement("h2");
          title.textContent = course.title;
  
          // Grades and Required Status
          const infoDiv = document.createElement("div");
          course.grades.forEach((grade) => {
            const gradeSpan = document.createElement("span");
            gradeSpan.className = `grade${grade}`;
            gradeSpan.textContent = grade;
            infoDiv.appendChild(gradeSpan);
          });
  
          if (course.required) {
            const reqSpan = document.createElement("span");
            reqSpan.className = "req";
            reqSpan.textContent = "Required";
            infoDiv.appendChild(reqSpan);
          }
  
          // Description
          const description = document.createElement("p");
          description.textContent = course.description;
  
          // Append elements to courseDiv
          courseDiv.appendChild(title);
          courseDiv.appendChild(infoDiv);
          courseDiv.appendChild(description);
          courseDiv.appendChild(document.createElement("hr"));
  
          // Append courseDiv to contentContainer
          contentContainer.appendChild(courseDiv);
        });
      })
      .catch((error) => console.error("Error loading content:", error));
  });
  