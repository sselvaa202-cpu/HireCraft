// ========================================
// HireCraft - Career Analysis Form
// ========================================

const careerForm = document.getElementById("career-analysis-form");

careerForm.addEventListener("submit", function (event) {

    // Prevent normal form submission
    event.preventDefault();

    // Get form values
    const formData = new FormData(careerForm);

    const careerProfile = {
        full_name: formData.get("full_name"),
        current_role: formData.get("current_role"),
        skills: formData.get("skills"),
        experience: formData.get("experience"),
        projects: formData.get("projects"),
        education: formData.get("education"),
        job_description: formData.get("job_description")
    };

    // Display collected data
    console.log("HireCraft Career Profile:");
    console.log(careerProfile);
});