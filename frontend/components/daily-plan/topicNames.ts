import { SubjectDetail } from "@/lib/api";

export function buildTopicNameMap(subjectDetails: SubjectDetail[]): Record<number, string> {
  const map: Record<number, string> = {};
  for (const subject of subjectDetails) {
    for (const unit of subject.units) {
      for (const topic of unit.topics) {
        map[topic.id] = topic.name;
      }
    }
  }
  return map;
}
