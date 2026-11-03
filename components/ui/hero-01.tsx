import HeroSection from "@/components/ui/hero-01-utils/hero";
import type { NavigationSection } from "@/components/ui/hero-01-utils/header";
import Header from "@/components/ui/hero-01-utils/header";
import BrandSlider, {
  BrandList,
} from "@/components/ui/hero-01-utils/brand-slider";
import type { AvatarList } from "@/components/ui/hero-01-utils/hero";

export default function AgencyHeroSection() {
  const avatarList: AvatarList[] = [
    { image: "/img/team-face-1.jpg" },
    { image: "/img/team-face-2.jpg" },
    { image: "/img/team-face-3.jpg" },
    { image: "/img/team-face-4.jpg" },
  ];

  const navigationData: NavigationSection[] = [
    { title: "Home", href: "#home", isActive: true },
    { title: "Services", href: "#services" },
    { title: "About us", href: "#about" },
    { title: "Our work", href: "#gallery" },
    { title: "Contact", href: "#contact" },
  ];

  // Text-only slider items: NAVA INTERIOR trades (no third-party logos).
  const brandList: BrandList[] = [
    { image: "", lightimg: "", name: "Interior painting" },
    { image: "", lightimg: "", name: "False ceilings" },
    { image: "", lightimg: "", name: "Carpentry & joinery" },
    { image: "", lightimg: "", name: "Waterproofing" },
    { image: "", lightimg: "", name: "Swimming pools" },
  ];

  return (
    <div className="relative">
      <Header navigationData={navigationData} />
      <main>
        <HeroSection avatarList={avatarList} />
        <BrandSlider brandList={brandList} />
      </main>
    </div>
  );
}
