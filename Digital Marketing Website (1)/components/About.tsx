import { ImageWithFallback } from "./figma/ImageWithFallback";
import { Button } from "./ui/button";
import { CheckCircle } from "lucide-react";

const achievements = [
  "Certified Google Partners",
  "Facebook Marketing Certified",
  "HubSpot Inbound Certified",
  "ISO 9001:2015 Quality Management"
];

export function About() {
  return (
    <section id="about" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div>
            <ImageWithFallback
              src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600&h=400&fit=crop"
              alt="Professional team meeting"
              className="rounded-2xl shadow-xl w-full h-96 object-cover"
            />
          </div>
          <div>
            <h2 className="text-3xl sm:text-4xl text-gray-900 mb-6">
              Why Choose DigitalPro?
            </h2>
            <p className="text-lg text-gray-600 mb-8 leading-relaxed">
              With over 5 years of experience in digital marketing, we've helped hundreds of 
              businesses transform their online presence and achieve remarkable growth. Our 
              team of certified experts stays ahead of industry trends to deliver cutting-edge 
              solutions.
            </p>
            
            <div className="space-y-4 mb-8">
              {achievements.map((achievement, index) => (
                <div key={index} className="flex items-center">
                  <CheckCircle className="h-5 w-5 text-green-500 mr-3" />
                  <span className="text-gray-700">{achievement}</span>
                </div>
              ))}
            </div>

            <div className="grid grid-cols-2 gap-8 mb-8">
              <div>
                <div className="text-2xl text-primary mb-2">15M+</div>
                <div className="text-gray-600">Impressions Generated</div>
              </div>
              <div>
                <div className="text-2xl text-primary mb-2">2.5x</div>
                <div className="text-gray-600">Average ROI Increase</div>
              </div>
            </div>

            <Button size="lg">Learn More About Us</Button>
          </div>
        </div>
      </div>
    </section>
  );
}