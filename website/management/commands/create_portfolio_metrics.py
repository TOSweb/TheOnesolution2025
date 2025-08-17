from django.core.management.base import BaseCommand
from website.models import Portfolio, PortfolioMetric


class Command(BaseCommand):
    help = 'Create sample portfolio metrics data for testing'

    def handle(self, *args, **options):
        self.stdout.write('Creating portfolio metrics...')
        
        # Get existing portfolios
        portfolios = Portfolio.objects.all()
        
        if not portfolios.exists():
            self.stdout.write(self.style.WARNING('No portfolios found. Please create portfolios first.'))
            return
        
        # Sample metrics data for each portfolio
        metrics_data = [
            {
                'metric_value': '300%',
                'metric_label': 'Traffic Increase',
                'metric_type': 'percentage',
                'order': 1
            },
            {
                'metric_value': '45%',
                'metric_label': 'Conversion Rate',
                'metric_type': 'percentage',
                'order': 2
            },
            {
                'metric_value': '2.5x',
                'metric_label': 'ROI Improvement',
                'metric_type': 'multiplier',
                'order': 3
            },
            {
                'metric_value': '2.1M',
                'metric_label': 'Revenue Generated',
                'metric_type': 'currency',
                'order': 4
            }
        ]
        
        for portfolio in portfolios:
            # Clear existing metrics
            portfolio.metrics_items.all().delete()
            
            # Create new metrics
            for metric_data in metrics_data:
                PortfolioMetric.objects.create(
                    portfolio=portfolio,
                    **metric_data
                )
            
            self.stdout.write(f'Created metrics for portfolio: {portfolio.title}')
        
        self.stdout.write(self.style.SUCCESS('Successfully created portfolio metrics!'))
