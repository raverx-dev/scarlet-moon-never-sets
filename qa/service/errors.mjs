export class QaInfrastructureError extends Error {
  constructor(code, message, evidence = {}) {
    super(message);
    this.name = 'QaInfrastructureError';
    this.code = code;
    this.evidence = evidence;
  }
}
