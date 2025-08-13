import { Button } from "./ui/button";
import { ImageWithFallback } from "./figma/ImageWithFallback";
import { ArrowRight, Play } from "lucide-react";

export function Hero() {
  return (
    <section className="bg-gradient-to-br from-gray-50 to-white py-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div>
            <h1 className="text-4xl sm:text-5xl lg:text-6xl tracking-tight text-gray-900 mb-6">
              Transform Your 
              <span className="text-primary"> Digital Presence</span>
            </h1>
            <p className="text-lg text-gray-600 mb-8 leading-relaxed">
              Elevate your business with our comprehensive digital marketing solutions. 
              From SEO to social media, we help you reach your target audience and drive 
              measurable results.
            </p>
            <div className="flex flex-col sm:flex-row gap-4">
              <Button size="lg" className="text-base px-8">
                Start Your Journey
                <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <Button variant="outline" size="lg" className="text-base px-8">
                <Play className="mr-2 h-5 w-5" />
                Watch Demo
              </Button>
            </div>
            <div className="mt-12 grid grid-cols-3 gap-8">
              <div>
                <div className="text-3xl text-primary mb-2">250+</div>
                <div className="text-gray-600">Happy Clients</div>
              </div>
              <div>
                <div className="text-3xl text-primary mb-2">98%</div>
                <div className="text-gray-600">Success Rate</div>
              </div>
              <div>
                <div className="text-3xl text-primary mb-2">5+</div>
                <div className="text-gray-600">Years Experience</div>
              </div>
            </div>
          </div>
          <div className="lg:pl-8">
            <ImageWithFallback
              src="https://images.unsplash.com/photo-1551434678-e076c223a692?w=600&h=400&fit=crop"
              alt="Team working on digital marketing strategy"
              className="rounded-2xl shadow-2xl w-full h-96 object-cover"
            />
          </div>
        </div>
      </div>
    </section>
  );
}