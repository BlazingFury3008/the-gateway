import React from 'react'

export default function Navbar_Link({title, link} : {title: string, link: string}) {
  return (
    <li className="relative group px-4 py-2 cursor-pointer">
    <a href={link} className='hover:underline'>
      {title}
    </a>
    </li>
  )
}
