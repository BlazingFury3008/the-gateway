import React, { useState } from 'react'

export default function BasicStats() {
  const [basicData, setBasicData] = useState({
    characterName: "",
    concept: "",
    ambition: "",
    desire: "",
    sire: "",
    generation: 11
  })


  return (
    <div className='sm:w-[90%] md:w-[80%] lg:2-[60%] mx-auto'>
      <div></div>
      <div className='grid md:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-4 mt-2'>
      <input
        type="text"
        placeholder="Character Name"
        className="input w-full"
        value={basicData.characterName}
        onChange={(e) => setBasicData({...basicData, characterName: e.target.value})}
        required
      />
            <input
        type="text"
        placeholder="Character Name"
        className="input w-full"
        value={basicData.concept}
        onChange={(e) => setBasicData({...basicData, concept: e.target.value})}
        required
      />
            <input
        type="text"
        placeholder="Character Name"
        className="input w-full"
        value={basicData.sire}
        onChange={(e) => setBasicData({...basicData, sire: e.target.value})}
        required
      />
            <input
        type="text"
        placeholder="Character Name"
        className="input w-full"
        value={basicData.ambition}
        onChange={(e) => setBasicData({...basicData, ambition: e.target.value})}
        required
      />
            <input
        type="text"
        placeholder="Character Name"
        className="input w-full"
        value={basicData.desire}
        onChange={(e) => setBasicData({...basicData, desire: e.target.value})}
        required
      />
            <input
        type="number"
        min={10}
        placeholder="Character Name"
        className="input w-full"
        value={basicData.generation}
        onChange={(e) => setBasicData({...basicData, generation: e.target.value})}
        required
      />
      </div>
    </div>
  )
}
