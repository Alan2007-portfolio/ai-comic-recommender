from models import Comic

comics = [
    Comic(
        id=1,
        title="Solo Leveling",
        type="manhwa",
        genres=["action", "fantasy"],
        setting="modern",
        tropes=["leveling system", "solo protagonist"],
        pacing="fast",
        art_style="detailed",
        tone="dark",
        summary="A weak hunter gains a mysterious leveling system and rises to become the strongest."
    ),
    Comic(
        id=2,
        title="The Extra's Academy Survival Guide",
        type="manhwa",
        genres=["fantasy", "academy"],
        setting="fantasy",
        tropes=["reincarnation", "side character"],
        pacing="medium",
        art_style="clean",
        tone="balanced",
        summary="A student reincarnates into a game world as a side character and must survive."
    ),
        Comic(
        id=3,
        title="Nano Machine",
        type="manhwa",
        genres=["action", "martial arts"],
        setting="murim",
        tropes=["revenge", "system"],
        pacing="fast",
        art_style="detailed",
        tone="dark",
        summary="A young martial artist receives a futuristic nanomachine that helps him rise in the murim world."
    ),

    Comic(
        id=4,
        title="Tales of Demons and Gods",
        type="manhua",
        genres=["fantasy", "action"],
        setting="fantasy",
        tropes=["reincarnation", "revenge"],
        pacing="fast",
        art_style="clean",
        tone="balanced",
        summary="A powerful spiritualist is reborn into his younger self and tries to change the future."
    ),

    Comic(
        id=5,
        title="Kingdom",
        type="manga",
        genres=["historical", "action"],
        setting="historical",
        tropes=["war", "strategy"],
        pacing="medium",
        art_style="detailed",
        tone="serious",
        summary="A war orphan dreams of becoming the greatest general during China's Warring States period."
    ),

    Comic(
        id=6,
        title="Martial Peak",
        type="manhua",
        genres=["martial arts", "fantasy"],
        setting="murim",
        tropes=["cultivation", "long journey"],
        pacing="slow",
        art_style="crowded",
        tone="balanced",
        summary="A young cultivator struggles to rise through endless martial realms."
    ),

    Comic(
        id=7,
        title="Attack on Titan",
        type="manga",
        genres=["action", "dark fantasy"],
        setting="post-apocalyptic",
        tropes=["war", "mystery"],
        pacing="fast",
        art_style="detailed",
        tone="dark",
        summary="Humanity fights for survival against giant humanoid creatures known as Titans."
    ),
    Comic(
        id=8,
        title="Death's game",
        type="manhwa",
        genres=["psychological", "thriller", "supernatural"],
        setting="modern",
        tropes=["multiple lives", "redemption", "consequences"],
        pacing="fast",
        art_style="clean",
        tone="dark",
        summary="A man who attempts suicide is punished by Death and forced to live multiple lives, each ending in death."
    ),    
    Comic(
        id=9,
        title="Omniscient Reader",
        type="manhwa",
        genres=["action", "fantasy"],
        setting="modern",
        tropes=["apocalypse", "knowledge advantage"],
        pacing="fast",
        art_style="clean",
        tone="dark",
        summary="A reader becomes the only person who knows how the world will end when his favorite novel turns into reality."
    ),

    Comic(
        id=10,
        title="The S-Class That I Raised",
        type="manhwa",
        genres=["action", "fantasy"],
        setting="modern",
        tropes=["regression", "monster hunters"],
        pacing="fast",
        art_style="clean",
        tone="balanced",
        summary="A weak hunter regresses and focuses on raising powerful S-class hunters instead of becoming strong himself."
    ),

    Comic(
        id=11,
        title="Return of the Mount Hua Sect",
        type="manhwa",
        genres=["martial arts", "action"],
        setting="murim",
        tropes=["reincarnation", "sect rebuilding"],
        pacing="medium",
        art_style="clean",
        tone="balanced",
        summary="A legendary martial artist reincarnates and returns to revive his fallen sect."
    ),

    Comic(
        id=12,
        title="Heavenly Demon Reborn",
        type="manhua",
        genres=["martial arts", "fantasy"],
        setting="murim",
        tropes=["reincarnation", "revenge"],
        pacing="fast",
        art_style="detailed",
        tone="dark",
        summary="A feared demon lord is reborn and seeks revenge while climbing the martial hierarchy again."
    ),

    Comic(
        id=13,
        title="Blue Lock",
        type="manga",
        genres=["sports", "psychological"],
        setting="modern",
        tropes=["competition", "survival"],
        pacing="fast",
        art_style="detailed",
        tone="intense",
        summary="A high-stakes soccer training program pushes players to become the ultimate ego-driven striker."
    ),

    Comic(
        id=14,
        title="Chainsaw Man",
        type="manga",
        genres=["action", "dark fantasy"],
        setting="modern",
        tropes=["devils", "anti-hero"],
        pacing="fast",
        art_style="detailed",
        tone="dark",
        summary="A boy merges with a devil and becomes a chainsaw-wielding hunter fighting supernatural threats."
    ),

    Comic(
        id=15,
        title="The World After the Fall",
        type="manhwa",
        genres=["action", "fantasy"],
        setting="apocalyptic",
        tropes=["tower climbing", "power system"],
        pacing="fast",
        art_style="clean",
        tone="dark",
        summary="After surviving a collapsing world, a lone climber challenges the system governing reality."
    ),

    Comic(
        id=16,
        title="Magic Emperor",
        type="manhua",
        genres=["fantasy", "action"],
        setting="fantasy",
        tropes=["reincarnation", "strategist"],
        pacing="medium",
        art_style="detailed",
        tone="dark",
        summary="A powerful demonic emperor is reborn into a weak body and uses strategy to reclaim dominance."
    ),

    Comic(
        id=17,
        title="Jujutsu Kaisen",
        type="manga",
        genres=["action", "supernatural"],
        setting="modern",
        tropes=["curses", "academy"],
        pacing="fast",
        art_style="detailed",
        tone="dark",
        summary="A high school student joins a secret sorcerer organization to fight cursed spirits."
    ),

    Comic(
        id=18,
        title="The Return of the Crazy Demon",
        type="manhwa",
        genres=["martial arts", "action"],
        setting="murim",
        tropes=["revenge", "eccentric protagonist"],
        pacing="fast",
        art_style="clean",
        tone="balanced",
        summary="A chaotic martial artist regresses and returns to the murim world with unpredictable methods."
    ),

    Comic(
        id=19,
        title="Doom Breaker",
        type="manhwa",
        genres=["fantasy", "action"],
        setting="fantasy",
        tropes=["regression", "revenge"],
        pacing="fast",
        art_style="clean",
        tone="dark",
        summary="A warrior chosen by the gods regresses after defeat and prepares to fight fate once again."
    ),

    Comic(
        id=20,
        title="Villain to Kill",
        type="manhwa",
        genres=["action", "superhero"],
        setting="modern",
        tropes=["revenge", "hidden identity"],
        pacing="fast",
        art_style="clean",
        tone="dark",
        summary="A hero framed for murder joins villains to uncover the truth and exact revenge."
    )
]