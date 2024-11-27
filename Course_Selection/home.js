// Get all questions
const questions = document.querySelectorAll('.question');
    
// Add click event to each question
questions.forEach(question => {
    question.addEventListener('click', function() {
        const answer = this.nextElementSibling;
        const arrow = this.querySelector('.arrow');
        
        // Toggle the visibility of the answer
        if (answer.style.display === "block") {
            answer.style.display = "none";
            arrow.style.transform = "rotate(0deg)"; // Rotate arrow back
        } else {
            answer.style.display = "block";
            arrow.style.transform = "rotate(180deg)"; // Rotate arrow down
        }
    });
});