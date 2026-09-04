# HireCraft - LinkedIn Content Intelligence Service

from app.schemas.linkedin_content import LinkedInContentPlan


def generate_linkedin_content_plan(
    target_role: str,
    required_skills: list[str],
) -> LinkedInContentPlan:
    """
    Generate LinkedIn content intelligence using only:

    - Target role
    - Required skills

    No existing LinkedIn profile data is used.
    No LLM is required.
    """

    target_role = target_role.strip()

    # Clean and deduplicate skills
    skills = []

    for skill in required_skills:
        if skill and skill.strip():
            clean_skill = skill.strip()

            if clean_skill.lower() not in [
                existing.lower() for existing in skills
            ]:
                skills.append(clean_skill)

    # 1. Content Pillars

    content_pillars = [
        target_role,
        "Technical Skills",
        "Software Development",
        "Project Building",
        "Professional Learning",
    ]

    # Add important skills as content pillars
    for skill in skills[:5]:
        if skill not in content_pillars:
            content_pillars.append(skill)

    # 2. General Post Topics

    post_topics = [
        f"Introduction to {target_role} and its core responsibilities.",
        f"Important skills required for a {target_role}.",
        f"Common development practices used by {target_role}s.",
        f"Career learning journey toward becoming a {target_role}.",
        f"Lessons learned while preparing for {target_role} opportunities.",
    ]

    # 3. Technical Post Ideas

    technical_post_ideas = []

    for skill in skills:
        technical_post_ideas.extend(
            [
                f"Beginner concepts every {target_role} should understand in {skill}.",
                f"Practical example of using {skill} in {target_role} development.",
            ]
        )

    if not technical_post_ideas:
        technical_post_ideas = [
            f"Technical concepts important for {target_role}.",
            f"Common technologies used in {target_role} development.",
            f"Best practices for writing maintainable {target_role} code.",
        ]

    # Limit excessive output
    technical_post_ideas = technical_post_ideas[:10]

    # 4. Project Post Ideas

    project_post_ideas = [
        f"Share a project demonstrating {target_role} skills.",
        "Explain the problem solved by a technical project.",
        "Explain the architecture and implementation of a project.",
        "Share the technologies used in a project and why they were selected.",
        "Share important lessons learned while building a project.",
        "Demonstrate a project feature with screenshots or a short demo.",
    ]

    # 5. Learning Post Ideas

    learning_post_ideas = [
        f"Share what you learned while preparing for {target_role}.",
        "Explain a technical concept you recently learned.",
        "Share a coding problem and explain how you solved it.",
        "Share mistakes made while learning and what you learned from them.",
        "Document progress while building a technical project.",
    ]

    # 6. Engagement Topics

    engagement_topics = [
        f"Follow discussions related to {target_role}.",
        "Comment on technical discussions related to the required skills.",
        "Engage with posts from software engineers and technical professionals.",
        "Discuss practical approaches to solving development problems.",
        "Share useful technical resources when relevant.",
        "Ask meaningful questions about technologies used in the target role.",
    ]

    # 7. 30-Day Content Direction

    thirty_day_content_direction = [
        "Week 1: Introduce your target career direction and core technical skills.",
        "Week 2: Share technical learning and practical development concepts.",
        "Week 3: Share project development, implementation and lessons learned.",
        "Week 4: Share project results, technical insights and career progress.",
    ]

    # 8. Return structured content plan

    return LinkedInContentPlan(
        content_pillars=content_pillars,
        post_topics=post_topics,
        technical_post_ideas=technical_post_ideas,
        project_post_ideas=project_post_ideas,
        learning_post_ideas=learning_post_ideas,
        engagement_topics=engagement_topics,
        thirty_day_content_direction=thirty_day_content_direction,
    )