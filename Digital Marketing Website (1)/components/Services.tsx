import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./ui/card";
import { Search, Share2, PenTool, BarChart3, Megaphone, Globe } from "lucide-react";

const services = [
  {
    icon: Search,
    title: "SEO Optimization",
    description: "Boost your search rankings with our proven SEO strategies and technical expertise."
  },
  {
    icon: Share2,
    title: "Social Media Marketing",
    description: "Engage your audience across all platforms with compelling content and targeted campaigns."
  },
  {
    icon: PenTool,
    title: "Content Creation",
    description: "Tell your brand story with high-quality content that resonates with your audience."
  },
  {
    icon: BarChart3,
    title: "Analytics & Insights",
    description: "Make data-driven decisions with comprehensive analytics and performance tracking."
  },
  {
    icon: Megaphone,
    title: "Paid Advertising",
    description: "Maximize your ROI with targeted Google Ads, Facebook Ads, and other PPC campaigns."
  },
  {
    icon: Globe,
    title: "Website Development",
    description: "Create stunning, responsive websites that convert visitors into customers."
  }
];

export function Services() {
  return (
    <section id="services" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl text-gray-900 mb-4">
            Our Digital Marketing Services
          </h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            We offer comprehensive digital marketing solutions tailored to help your business 
            grow and succeed in the digital landscape.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {services.map((service, index) => {
            const Icon = service.icon;
            return (
              <Card key={index} className="hover:shadow-lg transition-shadow duration-300">
                <CardHeader>
                  <div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
                    <Icon className="h-6 w-6 text-primary" />
                  </div>
                  <CardTitle className="text-xl">{service.title}</CardTitle>
                </CardHeader>
                <CardContent>
                  <CardDescription className="text-gray-600 leading-relaxed">
                    {service.description}
                  </CardDescription>
                </CardContent>
              </Card>
            );
          })}
        </div>
      </div>
    </section>
  );
}