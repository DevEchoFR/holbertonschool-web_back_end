export default function updateStudentGradeByCity(arr, city, newGrades) {
	if (!Array.isArray(arr) || !Array.isArray(newGrades)) {
		return [];
	}
	return arr.filter((student) => student.location === city).map((student) => {
		const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
		return {
			...student,
			grade: gradeObj ? gradeObj.grade : 'N/A',
		};
	});
}
