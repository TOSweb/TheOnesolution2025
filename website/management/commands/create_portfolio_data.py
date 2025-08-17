from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from website.models import PortfolioCategory, Portfolio
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Create sample portfolio data for testing'

    def handle(self, *args, **options):
        self.stdout.write('Creating portfolio categories...')
        
        # Create portfolio categories
        categories_data = [
            {
                'name': 'E-commerce',
                'description': 'E-commerce website development and optimization projects',
                'meta_title': 'E-commerce Portfolio - The One Solution',
                'meta_description': 'View our successful e-commerce projects and case studies',
            },
            {
                'name': 'Social Media Marketing',
                'description': 'Social media marketing campaigns and strategies',
                'meta_title': 'Social Media Marketing Portfolio - The One Solution',
                'meta_description': 'Explore our social media marketing success stories',
            },
            {
                'name': 'SEO Optimization',
                'description': 'Search engine optimization and organic traffic growth',
                'meta_title': 'SEO Portfolio - The One Solution',
                'meta_description': 'See our SEO optimization results and case studies',
            },
            {
                'name': 'PPC Campaigns',
                'description': 'Pay-per-click advertising and Google Ads campaigns',
                'meta_title': 'PPC Portfolio - The One Solution',
                'meta_description': 'View our PPC campaign results and success stories',
            },
            {
                'name': 'Web Design',
                'description': 'Website design and development projects',
                'meta_title': 'Web Design Portfolio - The One Solution',
                'meta_description': 'Explore our web design projects and case studies',
            },
        ]
        
        categories = {}
        for cat_data in categories_data:
            slug = slugify(cat_data['name'])
            category, created = PortfolioCategory.objects.get_or_create(
                slug=slug,
                defaults=cat_data
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')
            categories[cat_data['name']] = category
        
        self.stdout.write('Creating portfolio items...')
        
        # Create portfolio items
        portfolios_data = [
            {
                'title': 'TechStart Inc. - Complete Digital Transformation',
                'client_name': 'TechStart Inc.',
                'category': categories['E-commerce'],
                'short_description': 'A comprehensive digital marketing campaign that transformed TechStart Inc.\'s online presence, resulting in unprecedented growth and market expansion.',
                'full_description': 'TechStart Inc. was struggling with low online visibility and poor conversion rates. We implemented a complete digital transformation including SEO optimization, social media marketing, and conversion rate optimization. The results were outstanding with significant improvements across all key metrics.',
                'challenge': 'Low online visibility, poor conversion rates, outdated website design, lack of social media presence.',
                'solution': 'Complete digital transformation including website redesign, SEO optimization, social media marketing, and conversion rate optimization.',
                'implementation': 'We started with a comprehensive audit of their current digital presence, redesigned their website for better user experience, implemented SEO best practices, launched social media campaigns, and optimized conversion funnels.',
                'results_summary': 'Achieved remarkable growth in traffic, conversions, and revenue through strategic digital marketing implementation.',
                'metrics': '300% Traffic Increase\n45% Conversion Rate\n2.5x ROI Improvement\n$2.1M Revenue Generated',
                'technologies_used': 'WordPress\nGoogle Analytics\nGoogle Ads\nFacebook Ads\nMailchimp',
                'project_duration': '6 months',
                'team_size': '5 members',
                'client_testimonial': 'The One Solution transformed our business completely. Our online presence has never been stronger, and the results speak for themselves.',
                'client_position': 'CEO',
                'client_company': 'TechStart Inc.',
                'meta_title': 'TechStart Inc. Digital Transformation Case Study',
                'meta_description': 'How we helped TechStart Inc. achieve 300% traffic increase and $2.1M revenue through digital transformation.',
                'project_type': 'DigitalMarketing',
            },
            {
                'title': 'RetailMax - Social Media Campaign',
                'client_name': 'RetailMax',
                'category': categories['Social Media Marketing'],
                'short_description': 'Comprehensive social media strategy that generated 2.5M+ impressions and increased brand engagement by 180%.',
                'full_description': 'RetailMax needed to increase their brand awareness and engagement on social media platforms. We developed a comprehensive social media strategy that included content creation, community management, and paid advertising campaigns.',
                'challenge': 'Low brand awareness, poor social media engagement, inconsistent posting schedule, lack of content strategy.',
                'solution': 'Comprehensive social media strategy with content calendar, community management, and paid advertising campaigns.',
                'implementation': 'We created a content calendar, designed engaging visual content, implemented community management strategies, and launched targeted paid advertising campaigns across multiple platforms.',
                'results_summary': 'Achieved significant increase in brand awareness and engagement through strategic social media marketing.',
                'metrics': '2.5M+ Impressions\n180% Engagement Increase\n45% Follower Growth\n3.2x Brand Mentions',
                'technologies_used': 'Facebook Business Manager\nInstagram Business\nTwitter Ads\nLinkedIn Campaign Manager\nCanva',
                'project_duration': '4 months',
                'team_size': '3 members',
                'client_testimonial': 'Our social media presence has completely transformed. The engagement and brand awareness we\'ve achieved is incredible.',
                'client_position': 'Marketing Director',
                'client_company': 'RetailMax',
                'meta_title': 'RetailMax Social Media Campaign Case Study',
                'meta_description': 'How we helped RetailMax achieve 2.5M+ impressions and 180% engagement increase through social media marketing.',
                'project_type': 'DigitalMarketing',
            },
            {
                'title': 'Creative Studio - SEO Transformation',
                'client_name': 'Creative Studio',
                'category': categories['SEO Optimization'],
                'short_description': 'Strategic SEO implementation that moved the website from page 3 to page 1 for 25+ target keywords.',
                'full_description': 'Creative Studio was struggling with poor search engine rankings and low organic traffic. We implemented a comprehensive SEO strategy that included technical optimization, content optimization, and link building.',
                'challenge': 'Poor search engine rankings, low organic traffic, technical SEO issues, lack of content optimization.',
                'solution': 'Comprehensive SEO strategy including technical optimization, content optimization, and link building.',
                'implementation': 'We started with technical SEO audit, optimized website structure, improved content quality, implemented local SEO strategies, and built quality backlinks.',
                'results_summary': 'Achieved significant improvement in search engine rankings and organic traffic through strategic SEO implementation.',
                'metrics': '25+ Keywords on Page 1\n150% Traffic Increase\n200% Lead Generation\n45% Bounce Rate Reduction',
                'technologies_used': 'Google Search Console\nGoogle Analytics\nSEMrush\nAhrefs\nYoast SEO',
                'project_duration': '8 months',
                'team_size': '4 members',
                'client_testimonial': 'Our search engine rankings have improved dramatically. We\'re now getting consistent organic traffic and qualified leads.',
                'client_position': 'Founder',
                'client_company': 'Creative Studio',
                'meta_title': 'Creative Studio SEO Transformation Case Study',
                'meta_description': 'How we helped Creative Studio achieve 25+ keywords on page 1 and 150% traffic increase through SEO optimization.',
                'project_type': 'DigitalMarketing',
            },
            {
                'title': 'HealthTech - PPC Campaign',
                'client_name': 'HealthTech',
                'category': categories['PPC Campaigns'],
                'short_description': 'Google Ads campaign optimization that reduced cost-per-click by 40% while increasing conversions by 65%.',
                'full_description': 'HealthTech was spending too much on Google Ads with poor conversion rates. We optimized their PPC campaigns to improve efficiency and increase conversions while reducing costs.',
                'challenge': 'High cost-per-click, low conversion rates, poor ad performance, inefficient budget allocation.',
                'solution': 'PPC campaign optimization with improved targeting, ad copy, and landing page optimization.',
                'implementation': 'We analyzed existing campaigns, improved keyword targeting, optimized ad copy, enhanced landing pages, and implemented conversion tracking.',
                'results_summary': 'Achieved significant cost reduction and conversion improvement through strategic PPC optimization.',
                'metrics': '40% CPC Reduction\n65% Conversion Increase\n2.8x ROAS Improvement\n35% Budget Efficiency',
                'technologies_used': 'Google Ads\nGoogle Analytics\nGoogle Tag Manager\nOptimizely\nHotjar',
                'project_duration': '3 months',
                'team_size': '3 members',
                'client_testimonial': 'Our PPC campaigns are now much more efficient. We\'re getting better results while spending less money.',
                'client_position': 'Marketing Manager',
                'client_company': 'HealthTech',
                'meta_title': 'HealthTech PPC Campaign Case Study',
                'meta_description': 'How we helped HealthTech achieve 40% CPC reduction and 65% conversion increase through PPC optimization.',
                'project_type': 'DigitalMarketing',
            },
            {
                'title': 'Restaurant Chain - Website Redesign',
                'client_name': 'Fresh Bites Restaurant',
                'category': categories['Web Design'],
                'short_description': 'Modern, mobile-first website redesign that improved user experience and increased online orders by 120%.',
                'full_description': 'Fresh Bites Restaurant had an outdated website that was not mobile-friendly and had poor user experience. We redesigned their website with a modern, mobile-first approach.',
                'challenge': 'Outdated website design, poor mobile experience, low online order conversion, slow loading times.',
                'solution': 'Modern, mobile-first website redesign with improved user experience and conversion optimization.',
                'implementation': 'We redesigned the website with modern design principles, implemented mobile-first responsive design, optimized for speed, and improved conversion funnels.',
                'results_summary': 'Achieved significant improvement in user experience and online order conversion through website redesign.',
                'metrics': '120% Online Orders\n90% Mobile Traffic\n45% Page Load Speed\n60% User Engagement',
                'technologies_used': 'WordPress\nElementor\nWooCommerce\nGoogle PageSpeed Insights\nGTmetrix',
                'project_duration': '2 months',
                'team_size': '4 members',
                'client_testimonial': 'Our new website looks amazing and our online orders have increased dramatically. The mobile experience is fantastic.',
                'client_position': 'Owner',
                'client_company': 'Fresh Bites Restaurant',
                'meta_title': 'Fresh Bites Restaurant Website Redesign Case Study',
                'meta_description': 'How we helped Fresh Bites Restaurant achieve 120% online order increase through website redesign.',
                'project_type': 'WebSite',
            },
        ]
        
        for portfolio_data in portfolios_data:
            slug = slugify(portfolio_data['title'])
            portfolio, created = Portfolio.objects.get_or_create(
                slug=slug,
                defaults=portfolio_data
            )
            if created:
                self.stdout.write(f'Created portfolio: {portfolio.title}')
            else:
                self.stdout.write(f'Portfolio already exists: {portfolio.title}')
        
        self.stdout.write(self.style.SUCCESS('Successfully created portfolio data!'))
