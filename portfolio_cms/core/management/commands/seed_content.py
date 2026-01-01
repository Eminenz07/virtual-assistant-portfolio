from django.core.management.base import BaseCommand
from whatido.models import Service
from testimonials.models import Testimonial
from experience.models import Experience
from skills.models import Skill
from certifications.models import Certification
from projects.models import Project
from blogs.models import BlogPost
from datetime import date

class Command(BaseCommand):
    help = 'Seeds the database with initial content from the static site'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Services
        services = [
            {
                'title': 'Virtual Assistant',
                'description': 'Providing professional writing support to help businesses manage their online presence effectively.'
            },
            {
                'title': 'Brand Storyteller',
                'description': 'Crafting compelling narratives that connect brands with their audience and drive engagement.'
            }
        ]
        for s in services:
            Service.objects.get_or_create(title=s['title'], defaults=s)
        self.stdout.write(f'Seeded {len(services)} Services')

        # Testimonials
        testimonials = [
            {
                'client_name': 'Samuel Ifeanyi',
                'designation': 'Technical Writer',
                'testimonial_text': 'Excellence excels in storytelling and editing, with a keen eye for detail and collaborative spirit. Her commitment, communication, and teamwork skills ensure timely task completion. I highly recommend Excellence for any role requiring exceptional storytelling and editing.'
            },
            {
                'client_name': 'Jadesola Peace',
                'designation': 'Head of JAVIMS',
                'testimonial_text': 'I noticed that you write so well, especially on LinkedIn. I am texting to ask if you would like to manage our organisation\'s LinkedIn page in particular. Let me know what you think.'
            }
        ]
        for t in testimonials:
            Testimonial.objects.get_or_create(client_name=t['client_name'], defaults=t)
        self.stdout.write(f'Seeded {len(testimonials)} Testimonials')

        # Experience
        experiences = [
            {
                'role': 'Social Media Associate',
                'company': 'Pureworker',
                'start_date': date(2024, 7, 1),
                'end_date': date(2024, 9, 30),
                'description': 'Assisted in managing and editing blog posts. Supported content team with social media captions. Strengthened writing/editing skills.',
                'is_current': False
            },
            {
                'role': 'Blog Writer',
                'company': 'JAVIMS',
                'start_date': date(2024, 1, 1),
                'end_date': None,
                'description': 'Write blog posts amplifying survivors stories. Create educational content aligned with SDGs. Contribute to online presence through storytelling.',
                'is_current': True
            },
            {
                'role': 'Social Media Team',
                'company': 'Afrikoinart',
                'start_date': date(2024, 6, 1),
                'end_date': date(2024, 8, 31),
                'description': 'Wrote scripts for video content. Developed creative social media captions. Collaborated on campaign messaging.',
                'is_current': False
            }
        ]
        for e in experiences:
            Experience.objects.get_or_create(company=e['company'], role=e['role'], defaults=e)
        self.stdout.write(f'Seeded {len(experiences)} Experiences')

        # Skills
        skills = [
            'Creative Writing', 'Editing & Proofreading', 'Scriptwriting', 
            'SEO Writing', 'Brand Storytelling', 'Research & Analysis',
            'Collaboration', 'Communication', 'Adaptability'
        ]
        for skill_name in skills:
            Skill.objects.get_or_create(name=skill_name, defaults={'proficiency': 100, 'category': 'tech'}) # Default cat
        self.stdout.write(f'Seeded {len(skills)} Skills')

        # Certifications
        certs = [
            {'title': 'Social Media Associate', 'issuer': 'Unknown', 'date_earned': date(2024, 1, 1)},
            {'title': 'Social Media Virtual Assistant', 'issuer': 'Unknown', 'date_earned': date(2024, 1, 1)}
        ]
        for c in certs:
            Certification.objects.get_or_create(title=c['title'], defaults=c)
        self.stdout.write(f'Seeded {len(certs)} Certifications')

        # Projects
        projects = [
            {
                'title': 'Acne Treatment',
                'description': 'HOW I GOT RID OF MY ACNE IN ONE MONTH...',
                'year': 2024,
                'link_live': 'https://docs.google.com/document/d/11kA6uE5x1CoZbXvyy-MEh0YPn_3Coeb-AfCPBzvKWRU/edit?usp=drivesdk'
            },
            {
                'title': 'Clothing Care',
                'description': 'DO YOUR CLOTHES FADE AFTER A WHILE!?',
                'year': 2024,
                'link_live': 'https://docs.google.com/document/d/1ix5wGJd4X3h3hjSCktRPAVV2R3kEwNJVPCbBdArHUfs/edit?usp=drivesdk'
            },
            {
                'title': 'Missed Opportunity',
                'description': 'Missed a $500 Opportunity Because I Wasnt Ready.',
                'year': 2024,
                'link_live': 'https://docs.google.com/document/d/1pp8n2CtecDqyBNyS-94raRY5iXD4ar_UXXlviNvVsdk/edit?usp=drivesdk'
            }
        ]
        for p in projects:
            Project.objects.get_or_create(title=p['title'], defaults=p)
        self.stdout.write(f'Seeded {len(projects)} Projects')

        # Blogs
        blogs = [
            {
                'title': 'How Storytelling Transforms Your Brand',
                'markdown_body': 'Effective brand storytelling connects with your audience on an emotional level and builds lasting relationships. Learn how to craft compelling narratives that resonate.',
                'published_date': date(2024, 7, 1),
                'tags': 'Brand Storytelling'
            },
             {
                'title': 'Building a Content Strategy That Works',
                'markdown_body': 'A well-planned content strategy is essential for any business looking to make an impact online. Discover the key elements that drive engagement and conversions.',
                'published_date': date(2024, 6, 15),
                'tags': 'Content Strategy'
            }
        ]
        for b in blogs:
             BlogPost.objects.get_or_create(title=b['title'], defaults=b)
        self.stdout.write(f'Seeded {len(blogs)} Blogs')

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
