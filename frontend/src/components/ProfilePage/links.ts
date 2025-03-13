import { Users, MessageSquare, Book, Bookmark, Mail, Settings } from "lucide-react";

export const links = [
  { title: "Characters", linkText: "View Characters", link: "/profile/characters", icon: Users },
  { title: "Posts", linkText: "View Posts", link: "/profile/posts", icon: MessageSquare },
  { title: "Forums", linkText: "View Forums", link: "/profile/forums", icon: Book },
  { title: "Saved Wikis", linkText: "View Saved Wikis", link: "/profile/wikis", icon: Bookmark },
  { title: "Messages", linkText: "View Messages", link: "/profile/messages", icon: Mail },
  { title: "Config", linkText: "View & Edit Custom Configs", link: "/profile/config", icon: Settings },
];
