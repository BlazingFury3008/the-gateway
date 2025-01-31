import React from 'react'
import Navbar_Subdropdown from './navbar_subdropdown'
import Navbar_Link from './navbar_link'

export default function Navbar() {
  return (
    <div className='h-16 bg-gray font-[family-name:var(--font-geist-mono)]'>
        <h3 className='text-center mt-2 text-lg'>
            The Gateway
        </h3>
        <div>
            <ul className='mx-2 flex gap-4 text-sm'>
              <Navbar_Link title={"Home"
              } link={'/'} />
                <Navbar_Subdropdown title='Wiki' domain_link="/wiki" sub_domains={[
                    {title: "Vampire: The Masquerade 5th Ed", link: "/VTM_5th_Ed"},
                    {title: "Hunter: The Reckoning 5th Ed", link: "/HTR_5th_Ed"},
                    {title: "Werewolf: The Apocalypse 5th Ed", link: "/WTA_5th_Ed"},
                ]} />
                                <Navbar_Subdropdown title='Character Creation' domain_link={"/cc"} sub_domains={[
                    {title: "Vampire: The Masquerade 5th Ed", link: "/VTM_5th_Ed"},
                    {title: "Hunter: The Reckoning 5th Ed", link: "/HTR_5th_Ed"},
                    {title: "Werewolf: The Apocalypse 5th Ed", link: "/WTA_5th_Ed"},
                ]} />
            </ul>
        </div>
    </div>
  )
}
