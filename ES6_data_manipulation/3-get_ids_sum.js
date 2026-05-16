export default function getStudentIdsSum(arr) {
	if (!Array.isArray(arr)) {
		return 0;
	}
	return arr.reduce((sum, student) => sum + student.id, 0);
}