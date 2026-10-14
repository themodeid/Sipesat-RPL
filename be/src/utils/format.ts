export function getMonthRomawi(monthIndex: number): string {
  const romawi = [
    'I', 'II', 'III', 'IV', 'V', 'VI',
    'VII', 'VIII', 'IX', 'X', 'XI', 'XII'
  ];
  return romawi[monthIndex] || 'I';
}

export function generateNomorSuratResmi(formatTemplate: string, sequence: number): string {
  const now = new Date();
  const year = now.getFullYear().toString();
  const monthRomawi = getMonthRomawi(now.getMonth());
  const seqFormatted = String(sequence).padStart(3, '0');

  return formatTemplate
    .replace('{NOMOR}', seqFormatted)
    .replace('{BULAN_ROMAWI}', monthRomawi)
    .replace('{TAHUN}', year);
}
