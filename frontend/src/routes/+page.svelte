<svelte:head>
	<title>Table to MongoDB converter</title>
</svelte:head>

<div class="flex flex-col items-center justify-center">
	<h1 class="mb-6 text-center">
		Table to <span class="text-green-700">MongoDB</span> converters
	</h1>
	<h3 class="mb-4 text-center font-semibold">From where do you want to convert?</h3>
	<div class="flex justify-end">
		<a
			href="/excelToMongo"
			class="duration-250 mx-4 mb-3 w-36 rounded-md border-[1.5px] border-black p-3 text-center font-bold shadow-[2.5px_3px_0_#000] outline-none transition-all hover:bg-green-700 hover:text-white hover:shadow-[5.5px_7px_0_#000] md:w-64"
			>Microsoft Excel</a
		>
		<a
			href="/sheetsToMongo"
			class="duration-250 mx-4 mb-3 w-36 rounded-md border-[1.5px] border-black p-3 text-center font-bold shadow-[2.5px_3px_0_#000] outline-none transition-all hover:bg-green-700 hover:text-white hover:shadow-[5.5px_7px_0_#000] md:w-64"
			>Google Sheets</a
		>
	</div>
</div>
